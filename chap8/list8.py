# 用 户 ： 钱坤
# 使 用 人：钱坤
# 目 的：学习 赚钱
# 开发时间：  11:16

# 字符串的切片操作
''' 字符串是不可变类型
    不具备增删改等操作
    切片操作将产生新的对象
'''
s='Hello,Python'
s1=s[:5] #从索引0开始到索引5结束 不包括5 步长为1
print(s1)
s2=s[6:]
print(s2)
s3='!'
newstr=s1+s3+s2
print(newstr)
print('--------------------')
print(s)
print(s1)
print(s2)
print(s3)
print(newstr)