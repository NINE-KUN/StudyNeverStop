'''客户端
接下来我们写一个简单的客户端实例连接到以上创建的服务。端口号为 9999。
socket.connect(hostname, port ) 方法打开一个 TCP 连接到主机为 hostname 端口为 port 的服务商。
连接后我们就可以从服务端获取数据，记住，操作完成后需要关闭连接。
完整代码如下：'''

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
    ———>阻塞等待连接请求(新套接字) <---三次握手--connect()
   |      |                                   |
   |    recv()<----------------------------send()
   |      |                                   |
    ————send()---------------------------->recv()
          |                                   |
        close()<---------------------------close()
'''

# 导入socket、sys模块
import socket
import sys

# 创建socket对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 获取本地主机名
host = socket.gethostname()

# 设置端口号
port = 9996

# 链接服务、指定主机和端口
s.connect((host, port))

while True:
    re_data=input()
    s.send(re_data.encode('utf-8'))
    data = s.recv(1024)
    print(data.decode('utf-8'))

# 接收服务器端发送的数据 小于1024字节的数据
# msg = s.recv(1024) #bat类型 需要转码为utf8
#
# s.close()
#
# print(msg.decode('utf-8'))
