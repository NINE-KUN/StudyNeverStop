# 用 户 ： 钱坤
# 使 用 人：钱坤
# 目 的：学习 赚钱
# 开发时间：  12:01

# 集合的数学操作
s1={10,20,30}
s2={20,30,40,50,60}
#(1)交集
print(s1.intersection(s2))
print(s1 & s2)

#(2)并集
print(s1.union(s2))
print(s1 | s2)

#(3)差集
print(s1.difference(s2))
print(s1-s2)

#(4)对称差集
print(s1.symmetric_difference(s2))
print(s1 ^ s2)