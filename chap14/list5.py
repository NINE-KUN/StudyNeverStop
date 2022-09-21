# 用 户 ： 钱坤
# 使 用 人：钱坤
# 目 的：学习 赚钱
# 开发时间：  12:15
import os.path
print(os.path.abspath('list4.py'))#获取文件或目录的绝对路径
print(os.path.exists('list4.py'),os.path.exists('list5.py'))#用于判断文件或目录是否存在，如果存在返回True,如果不存在返回False
print(os.path.join('E:\\Python','list5.py'))#将目录与目录或文件名拼接起来
print(os.path.split('E\\Python\\chap14\\多态.py'))#将目录与文件拆分
print(os.path.splitext('list5.py'))#拆分文件与后缀名
print(os.path.basename('E\\Python\\chap14\\多态.py'))#从一个目录中提取文件名
print(os.path.dirname('E\\Python\\chap14\\多态.py'))#从一个路径中提取文件路径，不包括文件名
print(os.path.isdir('E\\Python\\chap14\\多态.py'))#用于判断是否为路径（list5是个文件）