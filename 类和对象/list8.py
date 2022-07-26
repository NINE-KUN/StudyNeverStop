# 用 户 ： 钱坤
# 使 用 人：钱坤
# 目 的：学习 赚钱
# 开发时间：  12:07
'''
__new__在前 为了创建对象
然后—__init__在后是为了给__new__的实例属性赋值
最后将创建的对象放在p1中存储
——————————————————————————————————————————————————
  传参方式：
   1.先将p1=Person('张三',20)中的Person('张三',20) 传给def __new__(cls, *args, **kwargs):中的cls
   2.然后将cls传参给obj中的__new__去创建对象
   3.然后将创建的对象赋值给self
   4.然后self传给p1
'''
class Person(object):
    def __new__(cls, *args, **kwargs):
        print('__new__被调用执行了，cls的id值为{0}'.format(id(cls)))
        obj=super().__new__(cls)
        print('创建的对象的id为：{0}'.format(id(obj)))
        return obj #obj返回给def __init__(self,name,age):中的self
    def __init__(self,name,age):
         print('__init__被调用了，self的id值为:{0}'.format(id(self)))
         self.name=name
         self.age=age

print('object这个类对象的id:{0}'.format(id(object)))
print('Person这个类对象的id为:{0}'.format(id(Person)))

#创建Person类的实例对象
p1=Person('张三',20)
print('p1这个Person类的实例对象的id:{0}'.format(id(p1)))
