'''从表现形式为
如果在一个内部函数里对外部作用域（但不是全局作用域）的变量引用'''
def FunX(x):
    def FunY(y): #对于 Funx Funy就是它的内部函数
        return x*y
    return FunY #FunY是一个闭包
# if __name__ == '__main__':
#     i=FunX(5)
#     print(i)
#     print(i(8))
#     print(FunX(5)(8))

'''内部函数不可对外部作用域的局部变量进行直接修改 如果要修改 可以使用容器 比如列表 字典等 或关键字nonlocal'''
# def Fun1():
#     x = 5
#     def Fun2():
#         x *= x #报错 未解析的引用x
#         return x
#     return Fun2()

'''使用容器'''
def Fun1():
    x = [5]
    def Fun2():
        x[0] *= x[0]
        return x[0]
    return Fun2()

'''使用关键字nolocal'''
def Fun3():
    x = 5
    def Fun4():
        nonlocal x #强制声明为不是局部变量
        x *= x
        return x
    return Fun4()

if __name__ == '__main__':
    print(Fun1())
    print(Fun3())
