# 用 户 ： 钱坤
# 使 用 人：钱坤
# 目 的：学习 赚钱
# 开发时间：  10:03
'''静态语言实现多态的的三个必要条件
     继承
     方法重写
     父类引用指向子类对象
     如java

     动态语言(Python)
       不需要考虑继承关系 只需要考虑是否含有该方法
'''
#多态
'''多态
    简单地说 多态就是具有多种形态 它是指 即便不知道一个变量所引用的对象到底是什么类型
    仍然可以通过这个变量调用方法 在运行过程中根据变量引用对象的类型
    动态决定调用哪个对象中的方法
'''
class Animal(object):
    def eat(self):
        print('动物会吃')
class Dog(Animal):
    def eat(self):
        print('狗吃骨头')
class Cat(Animal):
    def eat(self):
        print('猫吃鱼')
class Person:
    def eat(self):
        print('人吃五谷杂粮')
#定义一个函数
def fun(obj):
    obj.eat()
#开始调用函数
fun(Cat())
fun(Dog())
fun(Animal())
print('-----------------')
fun(Person()) #不用考虑Person是谁的子类 只需要关心它是否有eat方法
