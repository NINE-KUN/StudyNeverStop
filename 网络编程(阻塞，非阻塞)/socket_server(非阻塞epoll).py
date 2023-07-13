import socket
import threading
from collections import deque
import select
import queue

"""
epoll
判断非阻塞调用是否就绪如果 OS 能做，是不是应用程序就可以不用自己去等待和判断了，就可以利用这个空闲去做其他事情以提高效率。
所以OS将I/O状态的变化都封装成了事件，如可读事件、可写事件。并且提供了专门的系统模块让应用程序可以接收事件通知。这个模块就是select。
让应用程序可以通过select注册文件描述符和回调函数。当文件描述符的状态发生变化时，select 就调用事先注册的回调函数。
select因其算法效率比较低，后来改进成了poll，再后来又有进一步改进，BSD内核改进成了kqueue模块，而Linux内核改进成了epoll模块。
这四个模块的作用都相同，暴露给程序员使用的API也几乎一致，区别在于kqueue 和 epoll 在处理大量文件描述符时效率更高。
鉴于 Linux 服务器的普遍性，以及为了追求更高效率，所以我们常常听闻被探讨的模块都是 epoll 。

 回调(Callback)
把I/O事件的等待和监听任务交给了 OS，那 OS 在知道I/O状态发生改变后（例如socket连接已建立成功可发送数据），它又怎么知道接下来该干嘛呢？只能回调。
需要我们将发送数据与读取数据封装成独立的函数，让epoll代替应用程序监听socket状态时，得告诉epoll：“如果socket状态变为可以往里写数据（连接建立成功了），
请调用HTTP请求发送函数。如果socket 变为可以读数据了（客户端已收到响应），请调用响应处理函数。”

"""
# 创建stocket对象
# !/usr/bin/env python
# -*- coding:utf-8 -*-
# 创建socket对象
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 设置IP地址复用
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# ip地址和端口号
# 获取本地主机名
host = socket.gethostname()

# 设置端口号
port = 9996
server_address = (host, port)
# 绑定IP地址
serversocket.bind(server_address)
# 监听，并设置最大连接数
serversocket.listen(10)
print("服务器启动成功，监听IP：", server_address)
# 服务端设置非阻塞
serversocket.setblocking(False)
# 超时时间
timeout = 10
# 创建epoll事件对象，后续要监控的事件添加到其中
epoll = select.epoll()
# 注册服务器监听fd到等待读事件集合
epoll.register(serversocket.fileno(), select.EPOLLIN)
# 保存连接客户端消息的字典，格式为{}
message_queues = {}
# 文件句柄到所对应对象的字典，格式为{句柄：对象}
fd_to_socket = {serversocket.fileno(): serversocket, }

while True:
    print("等待活动连接......")
    # 轮询注册的事件集合，返回值为[(文件句柄，对应的事件)，(...),....]
    events = epoll.poll(timeout)
    if not events:
        print("epoll超时无活动连接，重新轮询......")
        continue
    print("有", len(events), "个新事件，开始处理......")

    for fd, event in events:
        socket = fd_to_socket[fd]
        # 如果活动socket为当前服务器socket，表示有新连接
        if socket == serversocket:
            connection, address = serversocket.accept()
            print("新连接：", address)
            # 新连接socket设置为非阻塞
            connection.setblocking(False)
            # 注册新连接fd到待读事件集合
            epoll.register(connection.fileno(), select.EPOLLIN)
            # 把新连接的文件句柄以及对象保存到字典
            fd_to_socket[connection.fileno()] = connection
            # 以新连接的对象为键值，值存储在队列中，保存每个连接的信息
            message_queues[connection] = queue.Queue()
        # 关闭事件
        elif event & select.EPOLLHUP:
            print('client close')
            # 在epoll中注销客户端的文件句柄
            epoll.unregister(fd)
            # 关闭客户端的文件句柄
            fd_to_socket[fd].close()
            # 在字典中删除与已关闭客户端相关的信息
            del fd_to_socket[fd]
        # 可读事件
        elif event & select.EPOLLIN:
            # 接收数据
            data = socket.recv(1024)
            if data:
                print("收到数据：", data, "客户端：", socket.getpeername())
                # 将数据放入对应客户端的字典
                message_queues[socket].put(data)
                # 修改读取到消息的连接到等待写事件集合(即对应客户端收到消息后，再将其fd修改并加入写事件集合)
                epoll.modify(fd, select.EPOLLOUT)
        # 可写事件
        elif event & select.EPOLLOUT:
            try:
                # 从字典中获取对应客户端的信息
                msg = message_queues[socket].get_nowait()
            except queue.Empty:
                print(socket.getpeername(), " queue empty")
                # 修改文件句柄为读事件
                epoll.modify(fd, select.EPOLLIN)
            else:
                print("发送数据：", data, "客户端：", socket.getpeername())
                # 发送数据
                socket.send(msg)

# 在epoll中注销服务端文件句柄
epoll.unregister(serversocket.fileno())
# 关闭epoll
epoll.close()
# 关闭服务器socket
serversocket.close()
