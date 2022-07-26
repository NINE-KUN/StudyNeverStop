#导入urllib库
from distutils.log import error
import imp
from telnetlib import PRAGMA_HEARTBEAT
from turtle import ht
from urllib import request,error
import re
#定义url地址，创建请求对象
url="http://www.baidu.com"
req=request.Request(url)#把url地址进行封装

try:
    #发起请求
    res=request.urlopen(req)
    #输出响应对象信息
    print(res.status)#请求返回结果状态码
    #print(res.version)#请求返回协议版本号
    #print(res.geturl())#获取请求页面(防止重定向)
    #print(res.getheaders())#获取响应头信息，返回二元元组列表
    #print(res.info())#获取响应头信息，返回字符串

    #获取相应对容
    html=res.read().decode("utf-8")#decode进行解码
    #解析内容
    print(re.findall("<title>(.*?)</title>",html))
except error.HTTPError as e:
    print("HTTPError")
    print(e.reason)
    print(e.code)
    print(e.__class__.mro())#获取当前对象类的继承关系
except error.URLError as e:#http 继承url 所以子类在上面 
    print("URLError")
    print(e.reason)