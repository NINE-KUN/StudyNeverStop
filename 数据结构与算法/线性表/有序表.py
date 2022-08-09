'''有序表 是一种数据项依照某种可比性质来决定列表中的位置 从小到大(表头-->表尾)
    在python中可适用与所有定义了_gt_方法即('>'操作符)的数据类型'''


class OrderedList:  # 创建空表
    '''表头指向None即为空表'''
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head==[]

    def size(self):
        return


