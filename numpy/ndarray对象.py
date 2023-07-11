import numpy as np

"""
    ndarray中的所有元素的类型都是相同的，而Python列表中的元素类型是任意的，
    所以ndarray在存储元素时内存可以连续，而python原生list就只能通过寻址方式找到下一个元素，
    这虽然也导致了在通用性能方面Numpy的ndarray不及Python原生list，
    但在科学计算中，Numpy的ndarray就可以省掉很多循环语句，代码使用方面比Python原生list简单的多。
    
    ndarray对象
    NumPy 定义了一个n维数组对象，简称 ndarray 对象，
    它是一个一系列相同类型元素组成的数组集合。
    数组中的每个元素都占有大小相同的内存块，使用索引或切片的方式可以获取数组中的每个元素。
    ndarray 对象有一个 dtype 属性，该属性用来描述元素的数据类型。
    ndarray 对象采用了数组的索引机制，将数组中的每个元素映射到内存块上，并且按照一定的布局对内存块进行排列，常用的布局方式有两种，即按行或者按列。
    
    创建ndarray对象
    通过 NumPy 的内置函数 array() 可以创建 ndarray 对象，其语法格式如下：
    numpy.array(object, dtype = None, copy = True, order = None,ndmin = 0)
"""

"""使用numpy创建数组"""

a = np.array([1, 2, 3])
b = np.array([[1, 2, 3], [4, 5, 6]])

print(a)
print(type(a))
print(b)
