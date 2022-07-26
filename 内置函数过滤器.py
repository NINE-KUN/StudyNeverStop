'''filter 把任何非True的筛选了'''


#
# def fil():
#     print(filter(None, [1, 0, False, True]))
#     print(list(filter(None, [1, 0, False, True])))
#
#
# if __name__ == '__main__':
#     fil()


def fil1(x):
    return x % 2


if __name__ == '__main__':
    temp = range(1, 11)
    show = filter(fil1, temp)
    print(list(show))
    print(fil1(4))

'''使用匿名函数lambda实现'''


def lam():
    lam1 = list(filter(lambda x: x % 2, range(10)))
    print(lam1)
    print(lambda x: x % 2, range(10))


if __name__ == '__main__':
    lam()

'''map 映射 两个参数 一个函数和一个可迭代的序列
将序列的每一个序列 作为函数的参数进行加工 将加工后的参数组成一个新的序列'''


def ma():
    print(list(map(lambda x: x * 2, range(10))))

if __name__ == '__main__':
    ma()
