# 用 户 ： 钱坤
# 使 用 人：钱坤
# 目 的：学习 赚钱
# 开发时间：  12:26

class Student:  #类名由一个或多个单词组成，要求每个单词的首字母大写，其余小写

    native_pace='成都' #直接写在类里的变量，称为类属性

    def eat(self): #在类之外定义的称为函数，在类之内定义的称为实例方法
        print('中午吃什么呢？')

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

#创建Student类的对象
Stu=Student('邹涛',20)
'''调用Student()类中的eat方法时有两种方式'''
Stu.eat() #第一种 对象名.方法名()
Student.eat(Stu) # 第二种 类名.方法名(类的对象)  实际上就是方法定义处的self

print(Stu.Name)
print(Stu.Age)
#类属性的使用方式
print(Student.native_pace)
stu1=Student('魏万卉',25)
stu2=Student('任子楠',24)
print(stu1.native_pace)
print(stu2.native_pace)
Student.native_pace='天津'
print(stu1.native_pace)
print(stu2.native_pace)
print('----------类方法的使用方式----------')
Student.cm()
print('----------静态方法的使用----------')
Student.methon()