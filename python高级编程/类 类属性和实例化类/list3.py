# 用 户 ： 钱坤
# 使 用 人：钱坤
# 目 的：学习 赚钱
# 开发时间：  11:55

#动态绑定和属性方法
'''Python是动态语言 在创建对象之后 可以动态地绑定属性和方法'''
'''一个Student类可以创建N个Student类的实例对象，每个实例对象的属性值不同'''
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age #self.name和self.age是Student类的所有对象都有的属性
    def eat(self):
        print(self.name+'在吃饭')
stu1=Student('钱坤',25)
stu2=Student('邹涛',24)
print(id(stu1))
print(id(stu2))
print('----------为stu2动态绑定属性----------')
stu2.gender='男' #只属于stu2 只适用于当前绑定的对象
print(stu2.name,stu2.age,stu2.gender)

print('-----------动态的绑定方法----------')
#正常方法
stu1.eat()
stu2.eat()
def show():
    print('定义在类之外的，称为函数')
stu1.show=show()
stu1.show()
stu2.show()#没有绑定show方法所以不可使用
