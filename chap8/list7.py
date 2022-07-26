# 用 户 ： 钱坤
# 使 用 人：钱坤
# 目 的：学习 赚钱
# 开发时间：  11:

# 字符串的比较操作
'''
  比较规则：
      首先比较两个字符串中的第一个字符串，如果相等则继续比较下一个字符，依次比较下去，
      直到两个字符串中的字符不相等，其比较结果就是两个字符串的比较结果，两个字符串中的所有后续字符将不再被比较
  比较原理
      两个字符进行比较时，比较的是其ordinal value(原始值)，调用内置函数ord可以得到指定字符的ordinal value。
      与内置函数ord对应的内置函数chr 调用内置函数chr时指定ordinal value可以得到其对应的字符
'''
print('apple'>'app') # True
print('apple'>'banana') # False
print(ord('a'),ord('b')) # a的原始值97 b的原始值98 97>98 false
print(chr(97),chr(98)) # a,b

'''
  ==与is的区别
  ==比较的是Value
  is比较的是id是否相等
'''
a=b='Python'
c='Python'
print(a==b)
print(a==c)

print(a is b,id(a),id(b))
print(a is c,id(a),id(c))

