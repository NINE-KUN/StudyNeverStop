"""yield关键字"""


def fun_1():
    yield 1  # 第一部执行
    yield from fun_2()  # 第二部执行fun_2()方法
    yield 2  # 第四步执行


def fun_2():
    yield 3  # 第三部执行
    yield 4


f1 = fun_1()
print(type(f1), f1)
for item in f1:  # 因为是生成器
    print(item)
