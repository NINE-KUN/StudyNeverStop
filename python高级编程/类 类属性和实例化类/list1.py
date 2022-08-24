# 用 户 ： 钱坤
# 使 用 人：钱坤
# 目 的：学习 赚钱
# 开发时间：  11:58

'''类：
     类是多个类似事物组成的群体统称，帮助我们快速理解和判断事物的性质
     Python中一切皆对象
   类的组成:
     1.类属性
     2.实列方法
     3.静态方法
     4.类方法
'''
class Student:  #类名由一个或多个单词组成，要求每个单词的首字母大写，其余小写
    native_pace='成都' #直接写在类里的变量，称为类属性

    #在类之外定义的称为函数，在类之内定义的称为实例方法
    def eat(self):
        print('中午吃什么呢？') #之内

    def __init__(self,name,age):
        self.Name=name #self.Name 称为实体属性，进行了一个赋值操作，将局部变量的name的值赋值给实体属性
        self.Age=age

    #静态方法
    @staticmethod
    def methon():
        print('我使用了staticmethod修饰，所以我是静态方法')

    #类方法
    @classmethod
    def cm(cls):
        print('因为我使用了classmethon修饰，所以我是类方法')


print(id(Student),type(Student),Student)

'''由此可见 type-->class-->obj(如type-->int-->1)
    object是最顶层的基类
    type继承object type又实例化obeject(形成闭环)type也实例化list、str等类 
    所以一切皆对象 一起继承obj'''
class A:
    pass
class B(A):
    pass
print(type(A))
print(type(B))

'''type也是一个类，同时type也是一个对象
'''