


class Rectangle:
    def __init__(self, length, width): #不要写return
        '''__init__(self[])在类被调用的时候 执行的方法'''
        self.length = length
        self.width = width

    def getPeri(self):
        return (self.length + self.width) * 2

    def getArea(self):
        return self.width * self.length


rect = Rectangle(3, 4)
print(rect.getPeri())
print(rect.getArea())

class CapStr(str):
    '''__new__(cls, *args, **kwargs):对象实例化的时候调用的第一个方法 第一个参数是类
         后面的参数会原封不动的传给__init__ 需要一个实例对象作为返回值 通常返回class类对象
         当继承一个不可变类型 但需要修改使用__new__'''
    def __new__(cls, string):
        string=string.upper() #在实例化之前就进行操作 让字符串大写
        return str.__new__(cls,string) #返回给实例化对象
a=CapStr('word hard')
print(a)


'''__del__(self)析构器 当垃圾回收机制自动销毁数据时(所有对它的引用都del时) 会自动使用__del__'''
class C:
    def __init__(self):
        print('我是__init__方法我被调用了')
    def __del__(self):
        print('我是__del__方法 我被调用了')






