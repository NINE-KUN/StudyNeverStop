# 用 户 ： 钱坤
# 使 用 人：钱坤
# 目 的：学习 赚钱
# 开发时间：  14:44
# 字符串中的大小写转换方法
''' 字符串时不可变序列 转换后会产生一个新的字符串 即id发生改变'''
s='hellow,python'
print(s,id(s))
a=s.upper() # 把字符串中的所有字符都转化为大写
print(a,id(a))
b=s.lower() # 把字符串中的所有字符转化为小写
print(b,id(b))
print(b == s) # 内容一致
print(b is s) # 内存(id)不一致

s2='Hello,Python'
print(s2.swapcase()) # 把字符串中的大写字母转换为小写 将小写字母转化为大写

s3='hello,WORLD,PYTHON'
print(s3.capitalize()) # 把字符串中的 第一个字符转化为大写 其他字符转化为小写
print(s3.title()) #把每一个字符串的 第一个字符转化为大写 其他字符为小写
