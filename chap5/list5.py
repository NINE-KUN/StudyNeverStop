# 用 户 ： 钱坤
# 使 用 人：钱坤
# 目 的：学习 赚钱
# 开发时间：  17:28

#列表元素删除操作

'''
 Remove(): 一次删除一个元素
           重复元素只删除第一个
           元素不存在 抛出异常 ValueError
'''
lst=[10,20,30,40,50,60,60,50,40]
lst.remove(40)
print(lst)

'''
 pop(): 删除一个指定位置上的元素
        指定索引不存在 抛出异常 IndexError
        不指定索引 删除列表最后一个元素
'''
print('原列表',lst)
lst.pop(7)
print(lst)

print('----------切片 创建一个新列表----------')
print('原列表',lst)
new_lst=lst[4:6]
print(new_lst)
print('----------不产生新列表----------')
lst[3:4]=[]
print(lst)

'''
 clear() 清空列表
'''
print('----------clear()清空且表----------')
lst.clear()
print(lst)

'''
 del 删除列表
'''
print('----------del 删除列表----------')
del lst
