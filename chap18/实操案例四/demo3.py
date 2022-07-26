#商品价格竞猜
import random
price=random.randint(1000,1500)#随机生成一个1000~1500的数
print('今日精彩的商品为小米扫地机器人：价格在[100,1500]之间')
guess=int(input())
if guess>price:
    print('大了')
elif guess<price:
    print('小了')
else:
    print('猜对了')
print('真实价格为',price)
