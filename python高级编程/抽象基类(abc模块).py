'''
抽象基类 (abc模块)：
    1.在这个基础的类中 设定好方法 所有继承该类的类都需要覆盖该类的方法
    2.抽象基类无法用来实例化
'''


# 应用场景 检查某个类是否有某种方法
class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __len__(self):
        return len(self.employee)


com = Company(['a', 'b', 'c'])
print((hasattr(com, '__len__')))  # 检查对象中是否有某个属性

# 我们在某些情况下希望判定某个对象的类型
from collections.abc import Sized

isinstance(com, Sized)

# 我们需要某个子类必须实现某些方法
'''比如实现了一个web框架 ，我们需要集成(缓存cache)
    我们希望将来可以用redis 或者cache 或者memorychache 来自定义组件来替换现有的
    所以要设计一个抽象基类 指定子类必须实现某些方法'''

# 如何去模拟一个抽象基类

'''方法一：最简单的实现方式 通过如果没有重新实现 就抛异常(raise NotImplementedError)
        在调用类方法时如果没有重新实现报错'''


class CacheBase():  # 抽象基类
    def get(self, key):
        raise NotImplementedError

    def set(self, key, value):
        raise NotImplementedError


class RedisCache(CacheBase):
    '''  def set(self,key,value):
          raise NotImplementedError 如果重写了set就不会报错'''
    pass


redis_cache = RedisCache()
redis_cache.set('key', 'value')  # 调用方法时报错

import abc

'''方法二: 在初始化的时候如果没有重写方法就会报错'''


class CacheBase(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get(self, key):
        pass

    @abc.abstractmethod
    def set(self, key, value):
        pass


class RedisCache(CacheBase):
    pass


redis_cache = RedisCache()  # 初始化(即实例化时)报错
