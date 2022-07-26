#pip install lxml
from lxml import etree
import requests
def base():
    url='http://www.baidu.com'
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'}
    reque=requests.get(url,headers=headers)
    e=etree.HTML(reque.text)#创建项
    info=e.xpath('//div[@id="s-top-left"]/a/text()')#通过xpath在网页中定位爬取内容位置
    print(info)

def B_li():
    url='https://www.bilibili.com/v/popular/rank/bangumi'
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'}
    requ=requests.get(url,headers=headers)
    e=etree.HTML(requ.text)
    name=e.xpath('/html/body/div/div/div/div/ul/li/div/div/a/text()')
    num=e.xpath('//div/span[@class="data-box"][1]/text()')
    like=e.xpath('//div/span[@class="data-box"][2]/text()')
    for na,nu,li in zip(name,num,like):#zip将多个数据一起进行遍历
        print(f'{na}==={nu.strip()}===={li.strip()}')#用于移除字符串头尾指定的字符（默认为空格）或字符序列。

B_li()