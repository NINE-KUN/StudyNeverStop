# 用 户 ： 钱坤
# 使 用 人：钱坤
# 目 的：学习 赚钱
# 开发时间：  11:59

# 集合
'''
   python中的内置函数
   与列表、字典一样都属于可变序列 可进行增删改
   集合是没有value的字典
'''

# 创建集合
print('----------第一种创建方式，直接创建----------')
s={1,2,3,3,5,4,5}
print(s,type(s)) # 创建集合时不可含有重复元素 集合会删除重复的元素

print('----------第二种创建方式 使用内置函数set()----------')
s1=set(range(6))
print(s1,type(s1)) # 集合是无序的

s2=set([3,4,54,56]) # 将列表转换为集合
print(s2,type(s2))

s3=set('python')
print(s3,type(s3))

s4=set((123,3,4,4,5)) #将元组转换为集合会删除重复元素
print(s4,type(s4))

s5=set({1,23,33,34,2}) #集合类型转换为集合类型
print(s5,type(s5))

'''
空集合的创建
'''
s6=set()
print(s6,type(s6))