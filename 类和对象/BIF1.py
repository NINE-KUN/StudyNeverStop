'''zip()函数 创建一个聚合多个可迭代对象的迭代器
   zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。'''
lst=[1,2,3,4,5,6,7,8,9]
a=iter(lst)
b=list(zip(a,a,a))
print(b)
'''以上代码简化 
   先使用iter()内置函数想序列转化为一个迭代器
   zip() 函数将确保可迭代对象按从左至右的顺序组合
   这样类似 zip(*[iter(s)]*n) 的惯用形式
   便可以将同一个迭代器重复迭代 N 遍
   实现将对象划分为 N 个长度块的效果
   与 zip 相反，zip(*) 可理解为解压，返回二维矩阵式'''
c=list(zip(*[iter(lst)] * 3))
print(c)


''' map() 会根据提供的函数对指定序列做映射。
    第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。
    map(function, iterable,...)'''
a1=list(map(lambda x:x**2,lst) )
print(a1)

''' filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。
    该接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判断，
    然后返回 True 或 False，最后将返回 True 的元素放到新列表中。'''

dic={'1':'qiankun','11':'27','111':'成都','1111':'18512205914'}
lst=sorted(dic.items(),key=lambda i :i[0],reverse=False)

print(lst)