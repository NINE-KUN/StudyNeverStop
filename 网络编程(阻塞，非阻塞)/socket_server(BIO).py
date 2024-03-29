'''socket（套接字）想当于对对osi应用层以下层进行了封装
    只着重于应用层与stocket之间的数据传输
    socket封装了(表示层、会话层、传输层、网络层、数据链路层、物理层)
    常用得http协议之下 可以使用tcp/ip得接口'''

'''定义一个变量 这样就具备了数据收发能力 
   AF_INET代表使用IPV4协议 AF_UNIX代表LINUX系统协议 AF_INET6代表IPV6协议 SOCK_STREAM代表TCP协议 SOCK_DGRAM代表UDP协议
   s = socket(AF_INET, SOCK_STREAM)'''

'''socket()函数
Python 中，我们用 socket() 函数来创建套接字，语法格式如下：

socket.socket([family[, type[, proto]]])
参数
family: 套接字家族可以是 AF_UNIX 或者 AF_INET
type: 套接字类型可以根据是面向连接的还是非连接分为SOCK_STREAM或SOCK_DGRAM
protocol: 一般不填默认为0.


Socket 对象(内建)方法
服务器端套接字
s.bind()	绑定地址（host,port）到套接字， 在AF_INET下,以元组（host,port）的形式表示地址。
s.listen()	开始TCP监听。backlog指定在拒绝连接之前，操作系统可以挂起的最大连接数量。该值至少为1，大部分应用程序设为5就可以了。
s.accept()	被动接受TCP客户端连接,(阻塞式)等待连接的到来
客户端套接字
s.connect()	主动初始化TCP服务器连接，。一般address的格式为元组（hostname,port），如果连接出错，返回socket.error错误。
s.connect_ex()	connect()函数的扩展版本,出错时返回出错码,而不是抛出异常
公共用途的套接字函数
s.recv()	接收TCP数据，数据以字符串形式返回，bufsize指定要接收的最大数据量。flag提供有关消息的其他信息，通常可以忽略。
s.send()	发送TCP数据，将string中的数据发送到连接的套接字。返回值是要发送的字节数量，该数量可能小于string的字节大小。
s.sendall()	完整发送TCP数据。将string中的数据发送到连接的套接字，但在返回之前会尝试发送所有数据。成功返回None，失败则抛出异常。
s.recvfrom()	接收UDP数据，与recv()类似，但返回值是（data,address）。其中data是包含接收数据的字符串，address是发送数据的套接字地址。
s.sendto()	发送UDP数据，将数据发送到套接字，address是形式为（ipaddr，port）的元组，指定远程地址。返回值是发送的字节数。
s.close()	关闭套接字
s.getpeername()	返回连接套接字的远程地址。返回值通常是元组（ipaddr,port）。
s.getsockname()	返回套接字自己的地址。通常是一个元组(ipaddr,port)
s.setsockopt(level,optname,value)	设置给定套接字选项的值。
s.getsockopt(level,optname[.buflen])	返回套接字选项的值。
s.settimeout(timeout)	设置套接字操作的超时期，timeout是一个浮点数，单位是秒。值为None表示没有超时期。一般，超时期应该在刚创建套接字时设置，因为它们可能用于连接的操作（如connect()）
s.gettimeout()	返回当前超时期的值，单位是秒，如果没有设置超时期，则返回None。
s.fileno()	返回套接字的文件描述符。
s.setblocking(flag)	如果 flag 为 False，则将套接字设为非阻塞模式，否则将套接字设为阻塞模式（默认值）。非阻塞模式下，如果调用 recv() 没有发现任何数据，或 send() 调用无法立即发送数据，那么将引起 socket.error 异常。
s.makefile()	创建一个与该套接字相关连的文件'''

'''服务端
我们使用 socket 模块的 socket 函数来创建一个 socket 对象。socket 对象可以通过调用其他函数来设置一个 socket 服务。
现在我们可以通过调用 bind(hostname, port) 函数来指定服务的 port(端口)。
接着，我们调用 socket 对象的 accept 方法。该方法等待客户端的连接，并返回 connection 对象，表示已连接到客户端。
完整代码如下：'''

import socket
import sys
import threading

'''         socket编程
        Server(服务器端)                    Client(客户端)

        Socket                                      
          |
        bind(协议、地址、端口)
          |
        listen(监听客户端socket请求)
          |
        accept()                           Socket
          |                                   |
    ———>阻塞等待连接请求(新套接字) <---三次握手--connect() 链接
   |      |                                   |
   |    recv()<----------------------------send() 
   |      |                                   |
    ————send()---------------------------->recv()
          |                                   |
        close()<---------------------------close()
'''

'''实时聊天和多用户链接 BIN(同步阻塞)  必须和客户端完成一次完整的通信 
比如：客户端———>服务端发送111 服务端——>客户端111 才可以开始下一个客户端与服务器通信
如果：客户端1————>服务端发送222 客户端2————>服务端发送222 然后服务端才返回信息的话 只能给客户端1返回信息 之后无法返回客户端2的信息 
        除非客户端1重新发送请求 此时不阻塞了 服务端返回的消息才会发送给客户端2
        (每一个客户端连接服务器都会创建一个线程)
    单线程：某个stocket会影响其他stocket处理
    多线程：每个客户端分配一个线程 客户端较多是造成资源浪费 '''
# 创建socket对对象
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 获取本地主机名
host = socket.gethostname()

port = 9996

# 绑定(协议、地址和端口)
serversocket.bind((host, port))
# 或者直接指定 serversocket.bind(('0.0.0.0',8000))

# 设置最大连接数、超过后排队
serversocket.listen()

# 单通道通讯
# clientsocket, addr = serversocket.accept()  # accept()方法中返回了sock和addr

# serversocket.accept()每次只能接收一个请求 一个请求进来之后就加入while True无法出来
#     所以当多用户连接时 就把每一个serversocket做一个线程


# 定义一个函数 将socket_client中的逻辑拿过来
def handle_sock(clientsocket, addr):
    while True:
        data = clientsocket.recv(1024)  # 接收数据 控制数据大小 数据为字符串
        print(data.decode('utf-8'))  # 接收数据后解码 返回字符串
        datastr = data.decode('utf-8')
        print('线程名称为:' + threading.current_thread().name)
        if datastr == 'bye':
            break
        else:
            re_data = input()
            clientsocket.send(re_data.encode('utf-8'))  # 将输入的字符串编码发送
    clientsocket.close()


while True:
    clientsocket, addr = serversocket.accept()  # 被动接受TCP客户端连接,(阻塞式)等待连接的到来
    print(f'conn:{clientsocket},addr:{addr}')

    # 用线程去处理新接收的链接(用户)
    client_thread = threading.Thread(target=handle_sock, args=(clientsocket, addr))
    print('线程名称为:' + threading.current_thread().name)
    client_thread.start()  # 启动线程

    # data = clientsocket.recv(1024)
    # print(data.decode('utf-8'))
    # re_data=input()
    # clientsocket.send(re_data.encode('utf-8'))
    # # clientsocket.close()
