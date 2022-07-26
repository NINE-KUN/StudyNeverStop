# '''求素数'''
# def _odd_iter():
#     n = 1
#     while True:
#         n = n + 2
#         yield n
# '''注意这是一个生成器，并且是一个无限序列。
#
# 然后定义一个筛选函数：'''
#
# def _not_divisible(n):
#     return lambda x: x % n > 0
# '''最后，定义一个生成器，不断返回下一个素数：'''
#
# def primes():
#     yield 2
#     it = _odd_iter() # 初始序列
#     while True:
#         n = next(it) # 返回序列的第一个数
#         yield n
#         it = filter(_not_divisible(n), it) # 构造新序列
# '''这个生成器先返回第一个素数2，然后，利用filter()不断产生筛选后的新的序列。
#
# 由于primes()也是一个无限序列，所以调用时需要设置一个退出循环的条件：'''
#
# # 打印1000以内的素数:
# for n in primes():
#     if n < 100:
#         print(n)
#     else:
#         break
#
#
#
#
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lst1 = lst[::-1]
print('lst:', lst)
print("lst1", lst1)
lst2 = str(lst1)
