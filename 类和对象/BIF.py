'''issubclass(class,classinfo)
    class 是classinfo的子类 就返回info（一个类是自身的子类）
    非严格性的检查 classinfo可以是一个元组 由class组成'''


class A:
    pass


class B(A):
    pass


a = issubclass(B, A)
print(a)
b = issubclass(B, B)
print(b)
c = issubclass(B, object)
print(c)


class C:
    pass


d = issubclass(B, C)
print(d)

'''isinstance(object,classinfo)
    检查一个实例对象是否属于类 
    object不是object对象 返回false
    如果classinfo不是元组 抛出异常
    '''
b1 = B()
isA = isinstance(b1, B)
print(isA)
isB = isinstance(b1, A)
print(isB)
isC = isinstance(b1, C)
print(isC)  # False b1不属于C
isD = isinstance(b1, (A, B, C))
print(isD)

'''hasattr(object,name)测试对象是否有指定属性
    object对象 name属性'''


class C:
    def __init__(self, x=0):
        self.x = x


c1 = C()
haA = hasattr(c1, 'x')
print(haA)
# haB=hasattr(c1,x)#x不转化为字符串 会识别为变量 引发NameError异常
# print(haB)

'''getattr(object,name[,default])
    返回对象指定属性值 如果设置default会输出default 否则抛出异常'''
geA = getattr(c1, 'x')
print(geA)
geB = getattr(c1, 'y', '您所访问的属性不存在')
print(geB)

'''serattr(object,name.value) 设置对象指定属性的值 如果不存在则创建该属性并赋值'''
setattr(c1, 'y', '赋值')
seA = getattr(c1, 'y', '您所访问的属性不存在但创建并赋值了')
print(seA)

'''delattr(object,name)删除对象中指定属性 如果不存在则抛出attrError'''
delA = delattr(c1, 'y')
print(delA)
delB = getattr(c1, 'y', '属性已被删除不存在')
print(delB)

'''property(fget=None获取属性, fest=None设置属性，del=None删除属性, doc=None)
    通过属性去设置定义属性'''


class D:
    def __init__(self, size=10):
        self.size = size

    def getSize(self):
        return self.size

    def setSize(self, value):
        self.size = value

    def delSize(self):
        del self.size

    x = property(getSize, setSize, delSize)


d1 = D()
# a=d1.getSize() 可用a=d1.x代替
b=d1.x
print(b)
c=d1.x=18
print(c)
'''del d1.x'''
