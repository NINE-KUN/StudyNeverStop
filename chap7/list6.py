# 用 户 ： 钱坤
# 使 用 人：钱坤
# 目 的：学习 赚钱
# 开发时间：  10:24

# 集合之间的关系

print('---------- 两个集合是否相等 用运算符==或！=进行判断----------')
s1={10,20,30,50,60}
s2={10,20,60}
s3={10,20,90}
print(s1==s2)
print(s2!=s3)

print('----------一个集合是否是另一个集合的子集 调用方法 issubset进行判断----------')
print(s2.issubset(s1)) # 一个集合包含另一个集合 就说另一个集合为该集合的子集
print(s3.issubset(s2))

print('----------一个集合是否另一个集合的超集 调用方法issuperset进行判断----------')
print(s1.issuperset(s2)) #一个集合包含另一个集合 就称该集合为另一个集合的超集
print(s2.issuperset(s3))

print('----------两个集合是否不存在交集 调用方法isdisjoint进行判断(该方法意为是否没有交集)----------')
print(s2.isdisjoint(s1))
print(s3.isdisjoint(s2)) #s3是否与s1没有交集
s4={100,200,300}
print(s4.isdisjoint(s1)) #s4是否与1没有交集 True