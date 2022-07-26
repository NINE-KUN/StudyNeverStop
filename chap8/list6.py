# 用 户 ： 钱坤
# 使 用 人：钱坤
# 目 的：学习 赚钱
# 开发时间：  10:47

# 字符串的常用操作
''' 字符串替换 replace()'''
s='Hello,Python'
print(s.replace('Python','C#'))

s1='Hello,Python,Python,Python'
print(s1.replace('Python','C#',2)) # replace中 第一个参数被替换的子串 第二个参数指定替换子串的字符串 第三个参数指定最大替换次数

''' join() 将列表或元组中的字符串合并为一个字符串'''
lst=['Hello','World','Python']
print(''.join(lst))
print('|'.join(lst))

lst2=('Hello','World','Python')
print('|'.join(lst2))

print('*'.join('Python'))


