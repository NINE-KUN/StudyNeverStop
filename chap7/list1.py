# 用 户 ： 钱坤
# 使 用 人：钱坤
# 目 的：学习 赚钱
# 开发时间：  16:15

# 元组
'''
   什么是元组
       python中的内置数据结构之一，是一个不可变序列
    不可变序列(没有增删改的操作)：
       1.字符串
       2.元组
    可变序列(可以对序列执行增删改操作):
       1. 列表
       2.字典
'''
print('----------可变序列，列表、字典----------')
lst=[10,20,30]
print(lst,id(lst))
lst.append(60)
print(lst,id(lst))

dic={'邹涛':10,'钱坤':20}
print(dic,id(dic))
dic['魏万卉']=30
print(dic,id(dic))

print('----------不可变序列：字符串、元组----------')
str='hello'
print(str,id(str))
str=str+'world'
print(str,id(str)) # id 发生改变

# 元组的创建

'''
   元组的创建方式
      1.直接小括号
      2.使用内置函数tuple()
      3.直接写入
      4.只包含一个元素的元组末尾要写，
'''
print('----------小括号创建----------')
t=('python','hello','world')
print(t,type(t))

print('----------使用内置函数tuple()创建----------')
t=tuple(('邹涛','钱坤','魏万卉'))
print(t,type(t))

print('----------直接创建----------')
t='阿坤','阿涛','阿卉'
print(t,type(t))

print('----------只包含一个元素的元组创建----------')
t='钱坤',
print(t,type(t))

# 空列表
lst=[]
lst1=list()

#空字典
dic={}
dic1=dict()

#空元组
t=()
t1=tuple()

print('空列表',lst,lst1)
print('空字典',dic,dic1)
print('空元组',t,t1)