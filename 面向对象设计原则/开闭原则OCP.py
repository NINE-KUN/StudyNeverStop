""" 开闭原则就是扩展开放，对修改关闭，也就是说需要增加新功能的时候只需要添加新的代码
    而不修改原有的代码 """

import numpy as np
from abc import ABC, abstractmethod


class Operations(ABC):
    """Operations"""

    def __init__(self, _list):
        self.list = _list

    """ 抽象方法，含有@abstractmethod装饰器的类不能直接实例化
        并且继承了该类的方法必须复写含有该装饰器的方法 未被装饰的不用写"""

    @abstractmethod
    def operation(self):
        pass


class computeMean(Operations):  # 继承父类Operations 重写operation方法
    def operation(self):
        """ Compute Mean"""
        # super(computeMean,self).operation()
        print(f"计算后的平均数{np.mean(self.list)}")


class computeMax(Operations):  # 继承父类Operations 重写operation方法
    def operation(self):
        """ Compute Max"""
        print(f"计算出的最大数{np.max(self.list)}")


_list = [1, 2, 3, 4, 5]
compute_max = computeMax(_list)
compute_max.operation()
compute_mean = computeMean(_list)
compute_mean.operation()


class Main:
    """定义一个类用于输出所有Operations的子类中的方法"""

    @staticmethod
    def get_operations(_list):
        for son_operation in Operations.__subclasses__():
            son_operation(_list).operation()


Main.get_operations([1, 2, 3, 4, 5])
