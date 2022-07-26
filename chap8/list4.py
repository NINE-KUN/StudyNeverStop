# 用 户 ： 钱坤
# 使 用 人：钱坤
# 目 的：学习 赚钱
# 开发时间：  15:58

# 字符串的劈分
'''split() 字符串的左劈分'''
s='Hello Wolrd Python'
print(s.split()) # 从字符串的左边开始劈分 默认的劈分字符为空字符串 返回值都是一个列表
s1='Hello|Wolrd|Python'
print(s1.split(sep='|')) # 通过参数spa指定劈分字符串是劈分符
print(s1.split(sep='|',maxsplit=1)) # 通过参数maxsplit指定劈分字符串的最大次数 经过最大次劈分之后 剩余的字符串会单独做为一部分

'''split() 字符串的右劈分'''
print(s.rsplit()) # 从字符串的右边开始劈分 默认的劈分字符为空字符串 返回值都是一个列表
print(s1.rsplit(sep='|')) # 通过参数spa指定劈分字符串是劈分符
print(s1.rsplit(sep='|',maxsplit=1))# 通过参数maxsplit指定劈分字符串的最大次数 经过最大次劈分之后 剩余的字符串会单独做为一部分