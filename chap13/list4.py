# 用 户 ： 钱坤
# 使 用 人：钱坤
# 目 的：学习 赚钱
# 开发时间：  16:33
# 在list中导入有包package1的模块model1
'''导入带有包的模块时注意事项
        使用import方式导入时 只能跟包名或模块名
'''
import package1.model1 as Am1 #Am1是模块package1.model1 的别名
print(Am1.a)
'''使用from...import方式可以导入 包 模块 函数 变量'''
'''from package1 import model2
from  package1.model2 import a
'''