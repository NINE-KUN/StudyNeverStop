# 用 户 ： 钱坤
# 使 用 人：钱坤
# 目 的：学习 赚钱
# 开发时间：  13:19

#列出指定目录下的所有文件

import os
path=os.getcwd() #获取当前目录
lst=os.listdir(path)#获取路径下所有文件包括目录
for filename in lst:
    if filename.endswith('.py'):#endswith 指以...结尾
        print(filename)
