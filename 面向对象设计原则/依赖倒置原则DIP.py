""" 该原则在面向对象的语境下指：
    高层模块不应该依赖于低层模块，二者均应该依赖其抽象。
    抽象不应该依赖细节，细节应该依赖于抽象。
    所谓抽象就是指接口类，细节就是实例化的接口类。
    依赖倒置原则指，面向对象编程的核心是面向接口编程，即不同类之间的依赖耦合在接口层上就已经实现。"""

from abc import abstractmethod, ABCMeta

"""抽象出 需要检查的类型父类(接口)"""


class opt_check(metaclass=ABCMeta):
    @abstractmethod
    def opt_check(self): pass


"""抽象出了检查的父类(接口)"""


class chk_check(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, optimizer: opt_check): pass  # 初始化检查接口的检查类型

    @abstractmethod
    def chk_check(self): pass  # 创建检查接口的的检查动作


""" 检查类型的子类 需要复写所有@abstractmethod声名了的父类动作
    两种检查类型 ase 和 dbs 继承检查父类opt_check(细节)"""


class ase_optimizer(opt_check):
    def opt_check(self):
        print('ase check')


class dbs_optimizer(opt_check):
    def opt_check(self):
        print('dbs check')


""" 检查接口的子类 
    需要复写父类所有@abstractmethod声明的动作(细节)"""


class checker(chk_check):
    def __init__(self, optimizer: opt_check):
        self.optimizer = optimizer

    def chk_check(self):
        self.optimizer.opt_check()


""" 可以看到，细节实现时，按照抽象的指示，填补空缺即可。此外，更高层调用高层时，依然满足依赖倒置原则"""


class auto_checker:
    @staticmethod
    def check(a_checker: checker):  # 实例化了checker类
        a_checker.chk_check()  # 调用checker的方法chk_check


a = auto_checker()
a.check(a_checker=checker(optimizer=ase_optimizer()))
a.check(a_checker=checker(optimizer=dbs_optimizer()))
