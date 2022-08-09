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
    temp = None(item) #先生成节点
    temp.setNext(self.head) #将临时节点设置为表头
    self.head = temp #再将表头设置为新增的节点
