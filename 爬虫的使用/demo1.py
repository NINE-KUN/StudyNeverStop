#url数据在哪
#发送请求
#接收到请求后=返回数据
#pip install requests
import requests
def spider1():
    url='https://www.bilibili.com'
    ''' get post都可以发送请求 如果直接从链接地址获取使用get 如果通过别的方式有可能使用post(一般获取数据用get 发送数据用post)
        通过网站检查中的 request method看请求方式
        reque=requests.get(url)
        requests.post(url)
    '''
    #伪装
    headers= {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'}
    reque=requests.get(url,headers=headers)#headers伪装成浏览器
    print("spider1",reque.text)
'''提取数据'''
#html标签：显示主要内容
#css：美化内容
#js：为了让页面更加好看，灵活性更强
#爬取b站番剧排行榜
def spider2():
    url='https://api.bilibili.com/pgc/web/rank/list?day=3&season_type=1'
    headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'}
    reque=requests.get(url,headers=headers)
    for i in reque.json().get('result').get('list'):
        print(i.get('title'))
spider2()