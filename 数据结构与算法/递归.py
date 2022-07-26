'''递归属于散发的内容
    是一个非常棒的编程思路
'''
# import sys
# sys.setrecursionlimit(10000) 设置递归深度为10000
'''如 谢尔宾斯基三角形
    汉诺塔
    递归：函数调用自身的行为
'''
# def recursion():
#     return recursion() #死循环 会无限调用直到小号所有内存
#
#
# if __name__ == '__main__':
#     recursion()

'''非递归版本阶乘'''


def recursion1(n):
    reslut = n
    for i in range(1, n):
        reslut *= i
    print(reslut)


if __name__ == '__main__':
    recursion1(5)

'''递归版本阶乘 递归条件 用调用自身的行为 有停止的条件'''
# def factorial(n):
#     if n==1:
#         return 1
#     else:
#         return n*factorial(n-1)
# number = int(input('请输入正整数'))
# result=factorial(number)
# print('%d 的阶乘是 %d'% (number,result))

'''斐波那契数列 使用递归'''


def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(10))

'''斐波那契数列 递归'''


def terfib(n):
    n1 = 1
    n2 = 1
    n3 = 0
    while n - 2 > 0:
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        n -= 1
    return n3


print(terfib(10))

'''分治思想
    
'''

'''汉诺塔'''


def hanoi(n, x, y, z):
    if n == 1:
        print(x, '-->', z)
    else:
        hanoi(n - 1, x, z, y)  # 将前n-1得盘子从x移动到y上
        print(x, '-->', z)  # 将最底下的最后一个盘子从x移动到z上
        hanoi(n - 1, y, x, z, )  # 将y上的n-1个盘子移动到z上





n = int(input('请输入汉诺塔得层数：'))
hanoi(n, 'x', 'y', 'z')
