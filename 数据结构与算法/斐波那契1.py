# 用 户 ： 钱坤
# 使 用 人：钱坤
# 目 的：学习 赚钱
# 开发时间：  12:03

'''斐波那契数列 前两项和等于第三项'''


def fib(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
#斐波那契额数列第6位上的数字
print(fib(6))

#斐波那契数列前6位上的数字
for i in range(1,7):
    print(fib(i))