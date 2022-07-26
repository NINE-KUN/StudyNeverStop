# 用 户 ： 钱坤
# 使 用 人：钱坤
# 目 的：学习 赚钱
# 开发时间：  12:30

# 面向对象的三大特征
'''封装：提高程序的安全性
        将数据(属性)和行为(方法)包装到类对象中。在方法内部对属性进行操作，在类对象的外部调用方法
        这样，无需关心方法内部的具体实现细节，从而隔离了复杂度
        在Python中没有专门的修饰符用于属性的私有，如果该属性不希望在类对象外部被访问，前边使用两个'__'

    继承:提高代码的复用性

    多态：提高程序的可拓展性和可维护性
'''

#封装
class Car:
    def __init__(self,brand):
        self.brand=brand
    def start(self):
        print('汽车启动')

car=Car('大G')
car.start()
print(car.brand)

class Student:
    def __init__(self,name,age):
        self.name=name
        self.__age=age
    def show(self):
        print(self.name,self.__age)
#创建对象 调用show方法
stu=Student('钱坤',25)
stu.show()
#在类的外部使用name和age
print(stu.name)
'''print(stu.age) 在Python中没有专门的修饰符用于属性的私有，如果该属性不希望在类对象外部被访问，前边使用两个'__' '''
print(dir(stu))
print(stu._Student__age) #在类的外部可以通过dir查询到封装的属性 并通过属性名进行访问 stu可以通过_Student__age访问age