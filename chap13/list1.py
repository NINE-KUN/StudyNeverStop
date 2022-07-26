# 用 户 ： 钱坤
# 使 用 人：钱坤
# 目 的：学习 赚钱
# 开发时间：  10:10
'''创建模块:
        新建一个.py文件 文件名称尽量不要与Python自带的标准模块名称相同
   导入模块：
        1.import  模块名称 [as别名]  (导入模块中所有)
        2.from 模块名称 import 函数/变量/类  (导入模块中指定)
'''
import math #关于数学运算
print(id(math))
print(type(math))
print(math)
print(math.pi)
print('--------------------------------------')
print(dir(math))
print(math.pow(2,3),type(math.pow(2,3))) #计算2的3次方

from math import pi
print(pi)
from math import pow
print(pow(2,3))
