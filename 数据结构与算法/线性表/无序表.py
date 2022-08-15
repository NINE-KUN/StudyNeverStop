'''无序表采用链表的方式实现 链表中每个数据元素 称之为一个节点
    一个节点包含数据本身以及指向下一个数据元素地址的next
    尾节点的next为None
    第一个节点和最后一个节点最重要 因为想要找到链表所有数据
    需要从第一个节点开始 直到找到节点的下一个元素地址为空(即尾节点)'''

'''链表样式 head(头指针)-->节点1(数据域(数据元素)+指针域(后继指针地质))-->节点2(数据域(数据元素)+指针域(后继指针地质因为为最后一个节点 指针域为None))'''

'''节点类'''


class Node:
    def __init__(self, initdata):  # 初始化节点时 将数据项传入 并将下一个节点赋为空
        self.data = initdata
        self.next = None

    def getDate(self):  # 返回数据项
        return self.data

    def getNext(self):  # 返回下一个节点
        return self.next

    def setData(self, newdata):  # 修改数据项
        self.data = newdata

    def setNext(self, newnext):  # 修改下一个节点的指向引用
        self.next = newnext


'''无序表必须要有对第一个节点的引用信息 即指向第一个节点的头节点 它的数据域没有值但是指针域会指向第一个节点的数据域地址
    设立一个属性head 保存对第一个节点的引用
    空表的head为None '''


class UnorderedList:  # 建立了一个空的无序表 isEmpty为Ture
    def __init__(self):
        self.head = None

    '''无序表的链表实现 根据最优性能 第一个节点加在尾部 最后一个节点加在头部'''

    def add(self, item):
        temp = Node(item)  # 先生成节点
        temp.setNext(self.head)  # 将临时节点设置为表头指向的结点
        self.head = temp  # 再将表头设置指向新增的节点

    def size(self):  # O(n)
        current = self.head  # 将当前节点设置为头结点指向结点(即第一个节点)
        count = 0  # 初始化一个计数器
        while current != None:  # 当节点不为空
            count = count + 1  # 计数器加1
            current = current.getNext()  # 将当前结点的下一节点设置为当前结点
        return count  # 返回计数器总和

    def search(self, item):
        current = self.head  # 初始化结点 将结点设置为表头所指结点(即)
        found = False
        while current != None and not found:
            if current.getData() == item:  # 判断结点是否为查询的结点
                found = True
            else:
                current = current.getNext()  # 将当前结点设置为下一结点
        return found

    '''
        删除时需要用双指针 当current指向第一个数据是 previous指向空 
        当current指向第二个节点时 previous指向第一个 (previous始终指向current上一个节点)
        当current指向要删除的节点时 将previous的下一节点改为current的下一个节点 即(previous.setNext(current.getNext()))
        '''

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None: # 判断删除的节点是不是第一个节点
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
