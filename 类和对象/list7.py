# 用 户 ： 钱坤
# 使 用 人：钱坤
# 目 的：学习 赚钱
# 开发时间：  12:29

a=20
b=100
c=a+b  # 两个整数类型的对象的相加操作
d=a.__add__(b)
print(c)
print(d)

class Student:
    def __init__(self,name):
        self.name=name
    def __add__(self, other):
        return self.name+other.name
    def __len__(self):
        return len(self.name)
stu1 = Student('钱坤')
stu2 = Student('邹涛')
s = stu1+stu2  # 实现了两个对象的加法运算 (因为在Student类中 编写了__add__()特殊方法)
print(s)
print('-------------------------')
lst=[11,22,33,44,55]
print(len(lst))
print(lst.__len__())
print(len(stu1))