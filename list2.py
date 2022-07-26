# 用 户 ： 钱坤
# 使 用 人：钱坤
# 目 的：学习 赚钱
# 开发时间：  0:35
# 变量 变量是内存中的一个带标签的盒子，需要将数据放进去
name = '钱坤'
print(name)
print('标识', id(name))
print('类型', type(name))
print('值', name)

# 变量多次赋值后会指向新的空间
Name = '钱坤'
print(Name)
Name = '阿坤'
print(Name)

# 数据类型
'''
 整型 int 如1024
 浮点型 float 如3.14
 布尔型 bool True/false
 字符串类型 str 如 钱坤一定能成功
'''

# 整型 可以表示 正数 负数 和 0
NaInt1 = 52
NaInt2 = -12
NaInt3 = 0
print(NaInt1, type(NaInt1), NaInt2, type(NaInt2), NaInt3, type(NaInt3))

# 整数可以表示为二级制 八进制 十进制 十六进制
print('二级制', 0b11011011)  # 二级制前要加0b
print('八进制', 0o256)  # 八进制前要加0o
print('十进制', 1024)  # 十进制
print('十六进制', 0x1EAF)  # 十六进制前要加0x

# 浮点型
FlName1 = 1.1
FlName2 = 2.2
print(FlName1, type(FlName1), FlName2, type(FlName2))

# 由于二级制计算 少量浮点型会出现错误 要计算时需要加入模块Decimal
print(FlName1+FlName2) # 运行结果出错 需加入模块运算
from decimal import Decimal
print(Decimal('1.1')+Decimal('2.2'))

# 布尔类型 True=1 False=0
BoName1 = True
BoName2 = False

print(True, type(BoName1))
print(BoName2, type(BoName2))

# 布尔类型可以进行计算
print(BoName1+1)  # 输出 1+1=2
print(BoName2+1)  # 输出 0+1=1

# 字符串类型
'''
 字符串又被称为不可变的字符序列
 可以使用 单引号’‘ 双引号“” 三引号’‘’ 或 三个双引号“”“ 来定义
 单引号和双引号必须在一行
 三引号和三个双引号可以连续多行使用
'''
str1 = '钱坤，一定能成为python大神'
str2 = "钱坤，一定能成为python大神 "
str3 = '''钱坤，
        一定能成为python大神'''
str4 = """钱坤，
        一定能成为python大神"""
print(str1, type(str1))
print(str2, type(str2))
print(str3, type(str3))
print(str4, type(str4))

# 字符串类型转换
name = '钱坤'
age = 25
print(type(name), type(age))
#  print('我叫'+name, '今年'+age)会报错 因为数据类型不同 需转化为同一数据类型进行输出
print('----------str()将其他类型转化为str类型----------')
print('我叫'+str(name), '今年'+str(age))
a = 10
b = 6.6
c = False
print(str(a), type(str(a)), str(b),type(str(b)), str(c), type(str(c)))

print('----------int()将其他类型转化为int类型----------')
s1 = 25
s2 = 63.5
s3 = '32'
s4 = False
s5 = '53.4'
s6 = 'HelloWorld'
print(int(s1), type(int(s1)))
print(int(s2), type(int(s2)))  # 当为float类型时 int（）转化为int类型时会截取整数部分，舍去小数部分
print(int(s3), type(int(s3)))
print(int(s4), type(int(s4)))
# print(int(s5), type(int(s5)))  # 无法转换 当把str类型转化为int类型时 str字符串必须为数字且是整数
# print(int(s6), type(int(s6)))  # 无法转换 当把str类型转化为int类型时 str字符串必须为数字且是整数

print('----------float（）将其他类型转化为float类型----------')
ss1 = 15
ss2 = 13.2
ss3 = '25'
ss4 = True
ss5 = '67.8'
ss6 = 'HelloWorld'
print(float(ss1), type(float(ss1)))  # 当转换int类型整数时 会在小数位加.0
print(float(ss2), type(float(ss2)))
print(float(ss3), type(float(ss3)))  # 当转换str类型时 且字符串为整数 会在转换后的整数后加.0
print(float(ss4), type(float(ss4)))  # 当转换bool类型时 会将bool类型转换为1/0并在转换后的整数后加.0
print(float(ss5), type(float(ss5)))
# print(float(ss6), type(float(ss6)))  # float()只能转化数字字符串

# 总结
'''
  str()将其他类型转化为str类型时 无规定
  int()将其他类型转化为int类型时 当为float类型时为截取整数位 截取小数位
                             当为str类型时 字符串必须为 整数 不可为小数或字符
  float()将其他类型转化为float类型时 会在转换后的整数后加.0 (不论是str类型整数，还是int类型整数)
                                 会将bool类型转换为1/0 并在后加.0
                                 float()无法转化文字                                                  
'''