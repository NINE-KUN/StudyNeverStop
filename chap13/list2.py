# 用 户 ： 钱坤
# 使 用 人：钱坤
# 目 的：学习 赚钱
# 开发时间：  10:27

#导入calc自定义模块 (需要右键单击chap 在Make Directory as中选择Sourcer Root)
import calc
print(calc.add(2,3))
print(calc.div(4,2))

from calc import add
print(add(3,3))
