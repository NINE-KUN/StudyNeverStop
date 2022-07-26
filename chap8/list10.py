# 用 户 ： 钱坤
# 使 用 人：钱坤
# 目 的：学习 赚钱
# 开发时间：  11:46

# 字符串的编码和解码

#编码
s='不要放弃你的浪漫主义'
print(s.encode(encoding='GBK')) # 在GBK这种编码格式中 一个中文占2个字节
print(s.encode(encoding='UTF-8')) #在UTF-8这种编码格式中，一个中文占3个字节

#解码
'''byte代表的是一个二进制数据(字节类型的数据)'''
byte=s.encode(encoding='GBK') #解码需和编码一直
print(byte.decode(encoding='GBK'))

byte=s.encode(encoding='UTF-8')
print(byte.decode(encoding='UTF-8'))