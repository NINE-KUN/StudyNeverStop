# 用 户 ： 钱坤
# 使 用 人：钱坤
# 目 的：学习 赚钱
# 开发时间：  16:09

s='Hello,Python'
'''isidentifier() 判断是否为合法的标识符 合法的标识符是 字母 数字 下划线 Hello，Python 含有，所以不是合法标识符'''
print('1.',s.isidentifier()) # False
print('2.','hello'.isidentifier()) #True
print('3.','钱坤_'.isidentifier()) #True
print('4.','钱坤_25'.isidentifier()) # True

'''isspace() 判断指定的字符串是否完全由空白字符组成（回车，换行，水平制表符）'''
print('5.','\t'.isspace()) #True

'''isalpha() 判断指定的字符串是否全部由字母组成'''
print('6.','Python'.isalpha()) #True
print('7.','钱坤'.isalpha()) # True
print('8.','钱坤25'.isalpha()) #False

''' isdecimal() 判断指定字符串是否全部由10进制组成'''
print('9.','123'.isdecimal()) #True
print('10.','123四'.isdecimal()) #False
print('11.','ⅡⅡⅡ'.isdecimal()) # False 罗马数字不是10进制

'''isnumeric() 判断指定字符串是否由数字组成'''
print('12.','123'.isnumeric()) #True
print('13.','123四'.isnumeric()) # True
print('14.','ⅡⅡⅡ'.isnumeric()) # True

''' isalnum() 判断指定字符串中是否全部由字母和数字组成'''
print('15.','abc1'.isalnum()) #True
print('16.','钱坤25'.isalnum()) #True
print('17.','abc!'.isalnum()) #False
