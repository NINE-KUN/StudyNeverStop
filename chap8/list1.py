# 用 户 ： 钱坤
# 使 用 人：钱坤
# 目 的：学习 赚钱
# 开发时间：  10:05

''' 字符串的驻留机制'''
'''
   驻留机制的几种情况(交互模式 cmd python)
      1.字符串的长度为0或1  如s1='' s2='k'
      2.符合标识符的字符串(字母或字母加下划线) 如s1='abc%' s2='abc%' 在交互模式中 不是同一个内存
      3.字符串只在编译时进行驻留，而非运行是 如 s1='abc' s2='ab'+'c'(在还未运行时已经编译为abc所以和s1是统一内存)
                        s3=''.join(['ab','c'])(在交互模式下s3 is not s1 因为s3在运行时才将'ac''c'结合为abc，开辟了新的内存空间)
      4.[-5,256]之间的整数
      5，在pyCharm中对字符串进行了优化会强制是两个相同的字符串不管在什么情况下都指向同一内存空间的对象
      6.sys中的intern 方法强制两个字符串指向同一个对象  如:s1='abc%' s2='abc%' 强制驻留写为 s1=sys.intern(b)                                 
'''
print('----------字符串的查找----------')
# index() 查找子串substr中第一次出现的位置，如果查找字串不存在时，则抛出异常ValueError
# rfindex() 查找子串substr中最后一次出现的位置，如果查找字串不存在时，则抛出异常ValueError
# find() 查找子串substr中第一次出现的位置，如果查找字串不存在时，则抛出异常-1
# rfind() 查找子串substr中最后一次出现的位置，如果查找字串不存在时，则抛出异常-1

s='hello,hello'
print(s.index('lo'))
print(s.rindex('lo'))
print(s.find('lo'))
print(s.rfind('lo'))

'''查找子串不存在时'''
#print(s.index('kk')) # ValueError: substring not found
#print(s.rindex('kk')) # ValueError: substring not found
print(s.find('kk')) #-1
print(s.rfind('kk')) #-1