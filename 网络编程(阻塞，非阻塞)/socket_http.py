#比如：requests库 实际上基于urlib完成得 urlib基于socket完成

'''通过socket去完成urlib当中获取get请求'''
import socket
from urllib.parse import urlparse

def get_url(url):
    #通过socket请求html

    #解析url
    url = urlparse(url)
    host=url.netloc
    path=url.path
    if path=="": #如果域名路径为空直接请求主域名
        path="/" #这个是http请求方式
    #新建socket链接
    clientsocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    clientsocket.connect((host, 80))#可以是ip加端口 也可以是域名加端口

    clientsocket.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path,host).encode("utf-8"))#http协议 比如百度 需要get host connection

    data=b"" #bate类型
    while True:
        d=clientsocket.recv(1024)#指定获取数据大小 如果大于1024
        if d:
            data +=d
        else:
            break
    data=data.decode("utf-8")
    html_data=data.split("\r\n\r\n")[1]
    print(html_data)
    clientsocket.close() #关闭连接
if __name__ == '__main__':
        get_url("http://www.baidu.com")