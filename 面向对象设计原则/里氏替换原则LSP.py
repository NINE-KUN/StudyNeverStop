""" 里氏替换原则
    父类能够使用的地方，将父类替换为子类，程序也能正常运行
    1.子类必须完全使用父类的方法
    2.子类可以有自己的个性
    3.覆写方法时，子类对应的参数类型范围只能比父类宽
    4.覆写方法时，子类对应的输出结果的类型只能比父类窄"""

from typing import Union
import numpy as np
from abc import ABC, abstractmethod

from typing import Union


class do_plus:
    def plus(self, addon: int) -> float:  # 父类的方法 参数类型为int 输出类型为float
        print(float(addon) + 1)


class math(do_plus):
    def plus(self, addon: Union[int, float]) -> float:  # 子类的方法 参数类型为int，float 输出类型为float
        return float(addon) + 1


a = do_plus()
a_results = a.plus(1)
# assert type(a_results) == float

b = math()
b_results = b.plus(1)
# assert type(b_results) == float
