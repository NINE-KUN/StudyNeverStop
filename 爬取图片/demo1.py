import requests
def download_img1():
    #url
    url='http://img.netbian.com/file/2021/0821/a49d58bea940c16ea6e5b2b2e159f687.jpg'
    #发送请求
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'}
    requ=requests.get(url,headers=headers)
    #接收保存
    with open('D:\\MoneyLoveLive\\爬取图片\\demo1.jpg','wb')as f:
        f.write(requ.content)
#爬取番剧排行榜图片
def download_img2():
    url='https://api.bilibili.com/pgc/web/rank/list?day=3&season_type=1'
    headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'}
    requ=requests.get(url,headers=headers)
    for i in requ.json().get('result').get('list'):#通过对网页的检查找到html中图片所在位置
        img_url=i.get('cover')
        title=i.get('title')
        img_re=requests.get(img_url,headers=headers)
        with open(f'D:\\MoneyLoveLive\\爬取图片\\{title}.jpg','wb') as f:
            f.write(img_re.content)
            f.close()
download_img2()