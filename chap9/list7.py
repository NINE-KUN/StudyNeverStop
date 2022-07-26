# 用 户 ： 钱坤
# 使 用 人：钱坤
# 目 的：学习 赚钱
# 开发时间：  12:03

def fun(a,b=10):
    print('a',a)
    print('b',b)

def fun1(*args1): #个数可变的位置形参
    print(args1)

def fun2(**args2): # 个数可变的关键字形参
    print(args2)

fun1(1,23,44,56,77)
fun2(a=12,b=23,c=33,d=55)
''' c，d采用关键字实参传递'''
def fun3(a,b,*,c,d): # 从*之后的参 在函数调用时 只能采用关键字参数传递
    print('a',a)
    print('b', b)
    print('c', c)
    print('d', d)
# fun3(10,20,30,40) #位置实参传递 报错
fun3(a=10,b=20,c=30,d=40) #关键字实参传递
fun3(10,20,c=30,d=40) # 前两个参数 采用的是位置实参传递 而c，d采用的是关键字实参传递

'''函数定义时形参的顺序问题'''
def fun4(a,b,*,c,d,**args):
    pass
def fun5(*args,**args1):
    pass
def fun6(a,b=10,*args1,**args2):
    pass

