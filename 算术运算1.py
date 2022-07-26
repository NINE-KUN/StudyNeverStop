class C :
    pass
print(type(C))
print(type(list))
print(type(int))
a=int('123')
print(a,type(a))
b=int('456')
print(a+b)

class New_int(int):
    def __add__(self, other):
        print(self) #3
        print(other) #5
        return int.__sub__(self,other)
    def __sub__(self, other):
        return int.__add__(self,other)
a=New_int(3)
b=New_int(5)
print(a+b) #调用New_int类 因为是+法 所以调用了 __add__方法 但是我们重写了方法让他返回减法方法计算的值 所以为-2
print(a-b) #同理 虽然调用的是减法方法 但是返回的是加法方法

class Try_int(int):
    def __add__(self, other):
        '''return self+other''' #会无限递归 a+b 进入__add__方法后 self+other又发现假发进入__add__
        return int(self)+int(other)
a=Try_int(3)
b=Try_int(5)
print(a+b) #会无限递归

'''
__sub__(self,other) -
__mul__(self,other) *
__truediv__(self,other) /
__floordiv__(self,other) //
__mod__(self,other) %
__divmod__(self,other) 定义当被divmod()调用时的行为 divmod(a,b) 返回值是一个元组(a//b,a%b)
__pow__(self,other[modulo]) 定义当被power()调用或**运算时的行为
__lshift__(self,other) 左移位 <<
__rshift__(self,other) 右移位 >>
__and__(self,other) 按位与 &
__xor__(self,other) 按位异或 ^
__or__(self,other) 按位或 |
'''