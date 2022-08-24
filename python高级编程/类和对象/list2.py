# 用 户 ： 钱坤
# 使 用 人：钱坤
# 目 的：学习 赚钱
# 开发时间：  14:57
#继承
'''语法格式
        class 子类类名(父类1，父类2...):
        pass
    如果一个类没有继承任何类，则默认继承object
    Python支持多继承
    定义子类时，必须在其构造函数中调用父类的构造函数
'''
class Person(object): #Person继承object类
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(self.name,self.age)

class Student(Person):
    def __init__(self,name,age,stu_no):
        super().__init__(name,age) #使用super调用父类中__init__方法
        self.stu_no=stu_no

class Teacher(Person):
    def __init__(self,name,age,teachofyear):
        super().__init__(name,age)
        self.teachofyear=teachofyear


stu=Student('钱坤',25,'20144901')
tea=Teacher('邹涛',24,'10')

stu.info()
tea.info()

#多继承
class A(object):
    pass
class B(object):
    pass
class C(A,B):
    pass