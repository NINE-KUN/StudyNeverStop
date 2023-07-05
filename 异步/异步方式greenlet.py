"""第一种：greenlet实现"""
from greenlet import greenlet


def fun_one():
    print('one')  # 第一步执行
    gr_two.switch()  # 第二部执行fun_two()方法
    print('two')  # 第五步执行
    gr_two.switch()  # 第六步执行gr_two()方法


def fun_two():
    print('tree')  # 第三步执行
    gr_one.switch()  # 第四步执行fun_one()方法
    print('four')  # 第七部执行


gr_one = greenlet(fun_one)
gr_two = greenlet(fun_two)

gr_one.switch()
