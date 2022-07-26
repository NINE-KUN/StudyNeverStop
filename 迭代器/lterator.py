'''
简介：

什么是迭代器？它是一个带状态的对象，在你调用next()方法的时候返回容器中的下一个值，任何实现了__iter__和__next__()（python2中实现next()）方法的对象都是迭代器，
__iter__返回迭代器自身，__next__返回容器中的下一个值，如果容器中没有更多元素了，则抛出StopIteration异常。
可迭代对象实现了__iter__方法，该方法返回一个迭代器对象，本文主要介绍一下Python中迭代器(Iterator)。

1、Python 迭代器(Iterator)
迭代器是一个包含数个值的对象。

迭代器是可以迭代的对象，这意味着您可以遍历所有值。

从技术上讲，在Python中，迭代器是实现迭代器协议的对象，该协议由方法__iter__()和__next__()组成。
'''

mytuple=('my','python','nb')
mylist=['my','python','nb']
myit=iter(mytuple)
print(myit)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(mytuple))
a=1

