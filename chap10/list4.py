# 用 户 ： 钱坤
# 使 用 人：钱坤
# 目 的：学习 赚钱
# 开发时间：  16:40
'''traceback模块 使用traceback模块打印异常信息'''
import traceback
try:
    print('--------------')
    print(1/0)
except:
    traceback.print_exc()


