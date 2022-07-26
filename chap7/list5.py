# 用 户 ： 钱坤
# 使 用 人：钱坤
# 目 的：学习 赚钱
# 开发时间：  12:51

# 集合的操作
'''
 判断元素是否在集合中 用in \ not in
'''
s={10,20,30,40}
print(10 in s)
print(90 in s)
print(10 not in s)
print(90 not in s)

'''
 像集合中增加元素
'''
s.add(50)  #向集合中添加一个元素
print(s)
s.update({11,12,13})  # 向集合中添加一个集合 update向集合中至少添加一个元素
print(s)
s.update([22,33]) #向集合中添加列表
print(s)
s.update((55,66,77)) #向集合中添加元组
print(s)

'''
  集合的删除操作
'''
s.remove(55) #一次删除一个指定元素 指定元素不存在抛异常
print(s)
#s.remove(909) KeyError: 909 指定元素不存在抛出异常

s.discard(22) #一次删除一个指定元素，元素不存在不抛出异常
print(s)

s.pop() # 一次删除一个任意元素 pop()中不可以包含参数
print(s)

s.clear() #清空元素
print(s)