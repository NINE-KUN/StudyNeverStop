'''有序表 是一种数据项依照某种可比性质来决定列表中的位置 从小到大(表头-->表尾)
    在python中可适用与所有定义了_gt_方法即('>'操作符)的数据类型'''


class OrderedList:  # 创建空表
    '''表头指向None即为空表'''

    def __init__(self):
        self.head = None
        self.next = None

    def getData(self):  # 返回数据项
        return self.data

    def getNext(self):  # 返回下一个节点
        return self.next

    def setData(self, newdata):  # 修改数据项
        self.data = newdata

    def setNext(self, newnext):  # 修改下一个节点数据项
        self.next = newnext

    def isEmpty(self):  # O(1)
        return self.head == []

    def size(self):  # O(n)
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = self.getNext()
        return count

    def remove(self, item):  # O(n)
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:  # 判断删除的节点是不是第一个节点
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def search(self, item):  # O(n)
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:  # 因为是有序链表 所以当前节点的数据项如果大于要找的数据项说明不存在 则stop=True
                    stop = True
                else:
                    current = current.getNext()
        return found

    """
        由于涉及的插入位置是当前节点之前，而单链表无法得到前驱
        所以跟remove类似 引入preious的引用，跟随当前节点current
        一旦找到了首个比插入数据项大的数据项，preious的nextData就赋值给指向查找节点(current= ) 而"""

    def add(self, item): #
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            '''发现插入位置'''
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()
        temp = OrderedList(item)
        if previous == None:  # 插入在表头
            temp.setNext(self.head)
            self.head = temp
        else:  # 插入在表中
            temp.setNext(current)
            previous.setNext(temp)
