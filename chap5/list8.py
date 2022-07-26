# 用 户 ： 钱坤
# 使 用 人：钱坤
# 目 的：学习 赚钱
# 开发时间：  15:15

#列表的创建 列表推导式 ()
'''注意：这可不仅仅是少写了一行代码而已，从程序的执行效率上来说，列表推导式的效率通常是要比循环语句快上一倍左右的速度。'''
lst=[i for i in range(1,11)]
print(lst)

print('----------创建一个列表，列表中元素为2，4，6，8，10')
lst=[i *2 for i in range(1,6)]
print(lst)


'''创建二维列表的错误方法  
   如果你试图修改其中的一个元素，就会发现有多个元素同时被修改了：'''
lstA=[[0]*3]*3
print(lstA)
lstA[1][1]=1
print(lstA) #这是因为内部嵌套的列表不是三个独立的列表，而是同一个列表的三次引用而已。

'''正确做法'''
lstB=[0]*3
for i in range(3):
    lstB[i]=[0]*3
lstB[1][1]=1
print(lstB)

'''更好的方法 用列表推导式'''
lstC=[[0]*3 for i in range(3)]
print(lstC)
lstC[1][1]=1
print(lstC)

'''带条件筛选功能的列表推导式
列表推导式其实还可以添加一个用于筛选的 if 分句，完整语法如下： [expression for target in iterable if condition1]'''

'''多层嵌套的列表推导式
列表推导式还可以变得更复杂一些，那就是实现嵌套，语法如下：
    [expression for target1 in iterable1
            for target2 in iterable2
            ...
            for targetN in iterableN]'''

'''每层嵌套还可以附带一个用于条件筛选的 if 分句：
    [expression for target1 in iterable1 if condition1
            for target2 in iterable2 if condition2
            ...
            for targetN in iterableN if conditionN]'''