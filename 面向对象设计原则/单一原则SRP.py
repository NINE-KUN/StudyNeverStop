"""一个类或者一个模块只负责完成一个职责（）（功能）"""

"""设计一个数学函数 计算最大值和平均值"""

import numpy as np


def math_operations(_list):
    # compute Average
    print(f"平均值是 {np.mean(_list)}")
    # compute Max
    print(f"最大值是 {np.max(_list)}")


math_operations(_list=[1, 2, 3, 4, 5, 6])

""" 在实际开发中 认为math_operations很庞大 杂揉了各种功能代码 
    所以更符合单一原则 将该函数拆分为多个颗粒度更细的函数 一个函数只干一件事
    
    易读易调试，更容易定位错误。

    可复用，代码的任何部分都可以在代码的其他部分中重用。

    可测试，为代码的每个功能创建测试更容易"""


class mathCompute(object):  # 首先抽象一个类
    # 抽象出类变量 用于维护基础数据
    def __init__(self, _list):
        self.list = _list

    # 抽象出类函数
    def get_mean(self):
        # Compute Average
        print(f"计算出的平均值为 {np.mean(self.list)}")

    def get_max(self):
        # Compute Max
        print(f"计算出的最大值为{np.max(self.list)}")


math_compute = mathCompute([1, 2, 3, 4, 5, 6])
math_compute.get_max()
math_compute.get_mean()
