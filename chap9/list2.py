# 用 户 ： 钱坤
# 使 用 人：钱坤
# 目 的：学习 赚钱
# 开发时间：  10:50

# 函数的定义
def fun(arg1,arg2):
    print('arg1',arg1)
    print('arg2',arg2)
    arg1=100
    arg2.append(10)
    print('arg1', arg1)
    print('arg2', arg2)
    return
# 函数的调用
'''在函数调用的过程中，进行参数的传递
如果是不可变对象，在函数体的修改不会影响实参的值(arg1的修改，不会影响n1的值)
如果是可变对象，在函数体的修改会影响到实参的值(arg2的修改，会影响n2的值)
'''
n1=11
n2=[22,33,44]
print('n1',n1)
print('n2',n2)
fun(n1,n2)  #将位置传参，arg1,arg2是函数定义处的形参。 n1,n2是函数调用出的实参 总结实参和形参可以不同名称
print('n1',n1)
print('n2',n2)