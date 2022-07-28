'''给定一个整数n（1<=n<=40)，输出一个边长为n的"*"字符构成的直角三角形图案。'''
def triangle(n):
    for Y in range(n):
        for X in range(Y + 1):
            print('*',end='\t')
        print()


if __name__ == '__main__':
    triangle(4)

'''给定一个整数n（1<=n<=20)，输出n的阶乘（=1*2*3*...*n）'''
def factorial(n):
    a=1
    b=0
    for i in range(n):
        b+=1
        a=a*b
    print(a)
def factorial1(n):
    if n==1:
        return 1
    else:
        return n*factorial1(n-1)
if __name__ == '__main__':
    print(factorial1(4))
    factorial(4)