# 用 户 ： 钱坤
# 使 用 人：钱坤
# 目 的：学习 赚钱
# 开发时间：  12:56

# 字典的常用操作(获取字典视图的三个方法）
'''
   获取字典视图
      keys() 获取字典中的所有key
      values() 获取字典中的所有value
      items() 获取字典中的所有key和value
'''
scores={'钱坤':26,'邹涛':25,'魏万卉':25}
keys=scores.keys()
print(keys,type(keys))
print(list(keys)) # 将所有key组成的视图转换成列表

values=scores.values()
print(values,type(values))
print(list(values)) # 将所有value组成的视图转换为列表

items=scores.items()
print(items,type(items))
print(list(items)) # 将所有key和value组成的视图转换为元组

'''
 字典的特点
     1.字典中的所有元素都是一个key-value对，key不允许重复，value可以重复
     2.字典中的元素是无序的
     3.字典中的key必须是不可变对象
     4.字典也可以根据需要动态的伸缩
     5.字典会浪费较大的内存，是一种使用空间换时间的数据结构
'''
# 字典的生成
names=['邹涛','钱坤','魏万卉']
ages=[25,26,27,24,27]
d={name.upper():age for name,age in zip(names,ages)}
print(d)
'''
 .upper()转义为大写
 value值多于key值从前匹配
'''