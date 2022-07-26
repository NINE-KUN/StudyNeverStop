
'''并集 先通过set转换为集合 通过集合方法union做并集 然后转换为列表'''
lst=[1,2,3,4,5,6]
lst3=[3,4,5,6,7,8]
l1=set(lst)
l2=set(lst3)
print(l1,l2)
print(list(l1.union(l2)))

'''线性表并集'''
def lst_union():
    lst2 = [3,4,5,6,7,8]
    for i in lst:
        if i not in lst2:
            lst2.append(i)
    return lst2
print(lst_union())


'''线性表的抽象数据类型描述'''
from abc import ABCMeta,abstractmethod,abstractproperty

class SqList():
    def __init__(self, maxSize):
        self.curLen = 6 # 顺序表的当前长度
        self.maxSize = maxSize # 顺序表的最大长度
        self.listItem = [1] * self.maxSize # 顺序表存储空间

    def clear(self):
        '''将线性表置成空表'''
        self.curLen = 0

    def isEmpty(self):
        '''判断线性表是否为空表'''
        return self.curLen == 0

    def length(self):
        '''返回线性表的长度'''
        return self.curLen

    def get(self, i):
        '''读取并返回线性表中的第i个数据元素'''
        if i < 0 or i > self.curLen - 1:
            raise Exception("第"+i+"个元素不存在")
        return self.listItem[i]

    def insert(self, i, x):
        '''插入x作为线性表中的第i个元素'''
        if self.curLen == self.maxSize:
            raise Exception("顺序表满")
        if i < 0 or i > self.curLen:
            raise Exception("插入位置非法")
        for j in range(self.curLen, i-1, -1):
            self.listItem[j] = self.listItem[j-1]
        self.listItem[i] = x
        self.curLen += 1

    def remove(self, i):
        '''删除线性表中的第i个元素'''
        if i < 0 or i > self.curLen - 1:
            raise Exception("删除位置非法")
        for j in range(i, self.curLen):
            self.listItem[j] = self.listItem[j+1]
        self.curLen -= 1

    def indexOf(self, x):
        '''返回元素x首次出现的位序号'''
        for i in range(self.curLen):
            if self.listItem[i] == x:
                return i
        return -1

    def display(self):
        '''输出线性表中各个元素的值'''
        for i in range(self.curLen):
            print(self.listItem[i], end=' ')

ilst=SqList(10)
print(ilst.display())
print(ilst.isEmpty())
print(ilst.length())
print(ilst.get(1))
print(ilst.insert(2,5))
print(ilst.remove(2))
print(ilst.indexOf(5))


