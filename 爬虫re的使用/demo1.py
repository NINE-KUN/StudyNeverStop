#re模块 正则表达式
'''
   re.match(pattern, string, flags=0)
    pattern	匹配的正则表达式
    string	要匹配的字符串。
    flags	标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。参见：正则表达式修饰符 - 可选标志

    我们可以使用 group(num) 或 groups() 匹配对象函数来获取匹配表达式。
        group(num=0)	匹配的整个表达式的字符串，group() 可以一次输入多个组号，在这种情况下它将返回一个包含那些组所对应值的元组。
        groups()	返回一个包含所有小组字符串的元组，从 1 到 所含的小组号。
'''
import re
str='I like Python3.8 every_day'
print('------------方法一match()--------------------')#从左到右开始依次比对如果有一个无法匹配则返回None
m1=re.match('I',str)#()第一个写表达(按正则表达式规则)式第二写从哪里取的数据
print(m1.group())#直接提取内容 而不返回对象
m2=re.match('I like (Python)',str)
print(m2.group(1))#表示提取第一个括号的内容
#通过通配符化来简便数据
m3=re.match('\w',str)#\w代表数字字母
m4=re.match('\S',str)#\S代表非空字符
m5=re.match('\D',str)#\D代表非数字
m6=re.match('.',str)#万能通配符. 代表任意字符
m7=re.match('.\s\w+',str)#万能通配符. 代表任意字符  一个符号代表一个字符 .表示I \s表示空格 \w+表示后边的like +代表一次或者多次 *代表0次或者多次
print(m3)
print(m4)
print(m5)
print(m6)
print(m7)
print('---------------------findall()--------------')#查找多次 根据规则相匹配的都查找出来
f1=re.findall('y',str)
print(f1)
print('------------search()---------------')#查找一次
s1=re.search('Python',str)#从任意位置开始匹配 只要符合就返回
s2=re.search('P\w+',str)#表示以字母p开始w+表示后面可以匹配多个字符
s3=re.search('P\w+.\d',str)#表示以字母p开始w+表示后面可以匹配多个字符
print(s1)
print(s2)
print(s3)
print(s3.group())

print('-----------------html--------------')
str2='<div><a class="title" href="http://www.bilibili.com">官网</a></div>'
h1=re.findall('href="http://www.bilibili.com">(官网)</a>',str2)#简单数据简单方法
print(h1)
'''通配符'''
h2=re.findall('href=".+">(.+)</a>',str2)
print(h2)



