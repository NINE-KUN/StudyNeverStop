# 这是一个注释符号
print('helloworld')
'''
这是多行注释符号
这是多行注释符号
'''
"""
这是多行注释符号
这是多行注释符号
"""
'''
print()函数 可以输出哪些内容
输出函数可以是数字
输出函数可以是字符串
输出函数可以是含有运算符表达式
print()函数 输出目的地
显示器
文件
print()函数 输出形式
换行
不换行
'''

# 输出数字
print(520)
print(98.5)

# 可以输出字符串
print('HelloWorld')
print("HelloWorld")

# 含有运算符表达式
print(3 + 1)

# 将数据输出至文件 注意点 1.所指定盘存在 2print（）函数后需file=一个变量
'''
open()函数标识符表

r 以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。

rb 以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。

r+ 打开一个文件用于读写。文件指针将会放在文件的开头。

rb+ 以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。

w 打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。

wb 以二进制格式打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。

w+ 打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。

wb+ 以二进制格式打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。

a 打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。

ab 以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。

a+ 打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。

ab+ 以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。

'''
fp = open("E:/MoneyLoveLive/text.txt", "a+")
print('HelloWorld', file=fp)
fp.close()

# 不进行换行输出（输出内容一行）
print('hello', 'world', 'and', 'python')

# 转义字符
'''
什么是转义字符
 就是反斜杠+想要实现的转移功能首字母
 
为什么需要转义字符
 当字符串中包含反斜杠、单引号、双引号等特殊用途的字符时，必须实用反斜杠对这些字符进行转义（转换一个含义）
 反斜杠：\\
 单引号：\‘
 双引号：\”

当字符串包含换行、回车、水平制表或退格等无法直接表示的特殊字符时，也可以使用转义字符
 换行：\n
 回车：\r
 水平制表符：\t
 退格：\b
'''
#\换行
print('hello\nworld')

# \t占用4个字符
print('hello\tworld')
print('helloooo\tworld')

# world 覆盖了hello
print('hello\rworld')

# 退一个格，将o退没了
print('hello\bworld')

# \\转义一个\
print('http:\\www.baidu.com')

# 想转义两个用\\\\
print('http:\\\\www.baidu.com')
print('老师说："大家好"')

# 原字符：不希望转义字符有效，在字符串前加r或R
print(r'hello\nworld')
# 注意事项 字符串后不能是一个反斜杠 会报错 如 print(r'hello\nworld\')

# 二进制 输出文字 乘 0b表示二进制 一个字符表示一个整数 这个整数会换算为二级制被计算机识别
print(chr(0b100111001011000))
print(ord('乘'))

# 保留字 一些单词被赋予了特定的意义 这些单词不可以给任何对象起名字
import keyword
print(keyword.kwlist)

# 标识符
'''
变量、函数、类、模块、其他对象的起的名字就叫标识符
规则：字母、数字、下划线
     不能以数字开头
     不能是保留字
     严格区分大小写
'''



