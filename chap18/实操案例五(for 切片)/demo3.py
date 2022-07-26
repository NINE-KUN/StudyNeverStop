#二分搜索法(猜数游戏)
import random #随机产生数
rand=random.randint(1,100)
for i in range(1,11):
    num=int(input('1-100，请你猜一猜'))
    if num<rand:
        print('小了')
    elif num>rand:
        print('大了')
    else:
        print('恭喜你，猜对了！')
        break
print(f'您一共猜了{i}次')
if i<3:
    print('聪明啊')
elif i<=7:
    print('还可以')
else:
    print('请学习二分搜索法(折半算法)')