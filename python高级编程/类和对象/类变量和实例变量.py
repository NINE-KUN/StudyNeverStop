'''
aa为类变量
'''
class A:
    aa=1 #类变量
    def __init__(self,x,y): #self指向这个类的实例
        self.x=x
        self.y=y

a=A(2,3)
print(a.x,a.y,a.aa)
print('A.aa',A.aa)
A.aa=11
print(a.aa)
a.aa=100 #一旦赋值 便生成实列a的新变量aa=100 而不去调用类中的aa (实例变量 )
print(a.aa)
print(A.aa)

print(range(1,3))