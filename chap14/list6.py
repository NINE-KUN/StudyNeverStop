# 用 户 ： 钱坤
# 使 用 人：钱坤
# 目 的：学习 赚钱
# 开发时间：  13:26
#遍历newdir所有文件
import os#导入os模块
path=os.getcwd()#获取当前工作目录
lst_file=os.walk(path)

for dirpath,dirname,filename in lst_file:
    for dir in  dirname:
        print(os.path.join(dirpath,dir))
        print('-------------------------------------')
    for file in filename:
        print(os.path.join(dirpath, file))
