# 用 户 ： 钱坤
# 使 用 人：钱坤
# 目 的：学习 赚钱
# 开发时间：  17:15

#列表元素的增加操作
'''
 paaend()在列表的末尾添加1个元素
'''
lst=[10,20,30,'hello','world']
print('添加元素之前',lst)
lst.append(40)
print('添加元素之后',lst)

'''
 extend()在列表的末尾至少添加一个元素
'''
lst2=['QianKun','Rich']
lst.append(lst2) #将lst2 作为一个元素添加至lst
print(lst)
lst.extend(lst2)
print(lst)

'''
 insert()  在列表的任意一个位置添加元素
'''
lst.insert(8,'very')
print(lst)

'''
 切片:在列表的任意位置至少添加一个元素
'''
lst3=[10,20,30,40,50,60]
lst4=[12,13,14,15]
lst3[3:]=lst4
print(lst3)
lst3[3]=lst4
print(lst3)
