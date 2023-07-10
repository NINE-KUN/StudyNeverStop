import socket
import threading
from collections import deque

"""
 BIO不会以为客户端的增加而分配线程 都在一个主线程运行 当客户端发送消息 服务器可以依次返回相应
 比如 客户端1————>服务器 发送111 同时 客户端2————>服务器 发送222 此时服务器可以返回响应111给客户端1 然后再给客户端返回响应222给客户端2
 不会产生阻塞（即不需要一次客户端与服务器完整的通信后才开始下一个客户端与服务器的通信）
"""
# 创建stocket对象
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # ipv4协议+tcp协议

# 设置为非阻塞
serversocket.setblocking(False)

# 获取本地主机名
host = socket.gethostname()

port = 9996

# 绑定(协议、地址和端口)
serversocket.bind((host, port))

# 设置最大连接数,超过后排队
serversocket.listen(5)

# 用于保存已经建立好的连接
connections = deque()

while True:
    try:
        conn, addr = serversocket.accept()
        print(f'conn:{conn},addr:{addr}')
        print("一个新客户端已连接：%s" % str(addr))
    except BlockingIOError as e:
        pass
    else:
        # 设置为非阻塞
        conn.setblocking(False)
        connections.append((conn, addr))
    for conn, addr in connections:
        try:
            data = conn.recv(1024)
            if len(data) > 0:
                print('来自', str(addr), '的信息', data)
                print(data.decode('utf-8'))
                datastr = data.decode('utf-8')
                print('线程名称为:' + threading.current_thread().name)
                if datastr == 'bye':
                    connections.remove((conn, addr))
                    print('%s 已下线' % str(addr))
                else:
                    re_data = input()
                    conn.send(re_data.encode('utf-8'))
            else:
                conn.close()
        except BlockingIOError as e:
            pass
