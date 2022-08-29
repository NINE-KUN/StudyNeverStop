'''socket（套接字）想当于对对osi应用层以下层进行了封装
    只着重于应用层与stocket之间的数据传输
    socket封装了(表示层、会话层、传输层、网络层、数据链路层、物理层)'''
from socket import *

'''定义一个变量 这样就具备了数据收发能力 
   AF_INET代表使用IPV4协议 SOCK_STREAM代表TCP协议 SOCK_DGRAM代表UDP协议
   s = socket(AF_INET, SOCK_STREAM)'''
