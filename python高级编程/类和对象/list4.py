# 用 户 ： 钱坤
# 使 用 人：钱坤
# 目 的：学习 赚钱
# 开发时间：  9:35

#object类
'''object类
      object类是所有类的父类 因此所有类都有object类的属性和方法

      内置函数dir()可以查看指定对象所有属性

      objec有一个_str_()方法 用于返回一个对于 对象的描述
      对应于内置函数str()经常用于print()方法 帮我们查看对象信息
      所以我们经常会对_str()_进行重写
'''
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return '我叫钱坤，今年25岁'
stu=Student('邹涛',24)# 默认调用__str__()这个方法
print(dir(stu))
print(stu) # 默认调用__str__()这个方法
print(type(stu))

