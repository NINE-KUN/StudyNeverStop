# 用 户 ： 钱坤
# 使 用 人：钱坤
# 目 的：学习 赚钱
# 开发时间：  9:25

#方法重写
'''方法重写
    如果子类对继承自父类的某个属性或方法不满意，可以在子类中对其(方法体)进行重新编写
    子类重写后的方法中可以通过super().xxx()调用父类中被重写的方法
'''
class Person(object): #Person继承object类
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(self.name,self.age)

class Student(Person):
    def __init__(self,name,age,stu_no):
        super().__init__(name,age)#使用super调用父类中__init__方法 super会自动找到基类名字（父类名字 ） 并且自动带有self参数
        #Person.__init__(self,name,age)#用父类类名调用父类中__init__方法
        self.stu_no=stu_no
    def info(self): #方法重写 将stu_no显示
        super().info()
        print(self.stu_no)

class Teacher(Person):
    def __init__(self,name,age,teachofyear):
        super().__init__(name,age)
        self.teachofyear=teachofyear
    def info(self):  #方法重写 将teachofyear显示
        super().info()
        print(self.teachofyear)

stu=Student('钱坤',25,'20144901')
tea=Teacher('邹涛',24,'10')

stu.info()
tea.info()
