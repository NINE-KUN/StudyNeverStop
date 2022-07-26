# 用 户 ： 钱坤
# 使 用 人：钱坤
# 目 的：学习 赚钱
# 开发时间：  10:51
'''
os模块是python内置的与操作系统功能和文件相关的模块，该模块中的语句的执行结果通常与操作系统有关，在不同的操作系统上运行，得到的结果可能不一样
os模块与os.path模块用于对目录或文件进行操作
'''
#os模块与操作系统相关的一个模块
import os
#os.system('notepad.exe')# 打开文本
#os.system('calc.exe')#打开计算器
#直接调用可执行文件
#os.startfile('E:\\Bin\\QQ.exe ')
print(os.getcwd())#返回当前的工作目录
lst=os.listdir('../chap14')#返回指定路径下的文件和目录信息
print(lst)

#os.mkdir('newdir1') #创建目录
#os.makedirs('A1/B/C')#创建多级目录

#os.rmdir('newdir')#删除目录
#os.removedirs('A/B/C')#删除多级目录

#os.chdir('path')#将path设置为当前工作目录
#print(os.getcwd())