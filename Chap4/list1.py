# 用 户 ： 钱坤
# 使 用 人：钱坤
# 目 的：学习 赚钱
# 开发时间：  20:32

# 内置函数range()
'''
 1.用于生成一个整数序列
 2.创建range对象的三种方式

 range(stop) 创建一个[0,stop]之间的整数序列，步长为1
 range(star,stop) 创建一个[star,stop]之间的整数序列，步长为1
 range(star,stop,step) 创建一个[star,stop,step]之间的整数序列，步长为step

 返回值是一个 迭代器对象
 优点：不管整数序列多长，占用内存空间都是相同的，因为只需要存储star,stop,step,只有当用到range对象时，才会计算序列中的相关元素
'''
r = range(10)
print(r)
print(list(r))

r = range(1, 10)
print(r)
print(list(r))

r = range(0, 10, 2)
print(r)
print(list(r))
print('----------用条件判断判断整数是否在序列中----------')
print(2 in r)
print(9 in r)

print(2 not in r)
print(9 not in r)

