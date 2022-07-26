# 用 户 ： 钱坤
# 使 用 人：钱坤
# 目 的：学习 赚钱
# 开发时间：  20:53

#循环结构
'''
选择结构IF与循环结构while的判断区别
 选择结构 IF是判断一次 条件为True执行一次
 循环结构 While是判断N+1次 条件为True执行N次
'''

'''TakeMoney = int(input('请输入取款金额'))
Money = int(100)
while Money > TakeMoney:
    print('取款成功')
    Money -= TakeMoney
'''
'''    a = 1
    while a < 10:
        print(a)
        a += 1'''


# 0-4之间的累加和
sum = 0
b = 0
while b < 5:
    sum += b
    b+= 1
    print('和为',sum)

sum = 0
b = 0
if b < 5:
    sum += b
    b+= 1
    print('和为',sum)


