# 用 户 ： 钱坤
# 使 用 人：钱坤
# 目 的：学习 赚钱
# 开发时间：  10:54

class A:
    pass
class B:
    pass
class C(A,B):
    def __init__(self,name,age):
        self.name=name
        self.age=age
#创建C类对象
x=C('Jack',25) #x是C类型的一个实例对象
print(x.__dict__) #实例对象的属性字典
print(C.__dict__)
print('-----------')
print(x.__class__)#输出了对象所属的类
print(C.__bases__)#C类的父类类型元组
print(C.__base__)
print(C.__mro__)#类的继承结构
print(A.__subclasses__())#A所包含的子类列表
