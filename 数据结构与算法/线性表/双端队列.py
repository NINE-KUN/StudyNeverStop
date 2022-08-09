'''双端队列Deque:
    跟队列相似，其两端可以称作 首 尾 端
    但deque中的数据项即可以从队首加入，也可以从队尾加入 数据项也可以从两端移除
    某种意义上说 双端队列集成了栈和队列的能力 如何进如何出 自己定义'''
'''
    双端队列抽象数据类型
    Deque():创建一个空的双端队列
    addFront(item):将item加入队首
    addRear(item):将item加入队尾
    removeFront():从队首移除数据，返回值为移除的数据项
    removeRear():从队尾移除数据项，返回值为移除的数据项
    isEmpty():返沪deque是否为空
    size():返回deque中包含的数据项个数
'''


class Deque():
    def __init__(self):
        self.items = []

    def addFront(self, item):
        self.items.append(item) #O(1)

    def addRear(self, item):
        self.items.insert(0, item)#O(n)

    def removeFront(self):
        return self.items.pop() #O(1)

    def removeRear(self):
        return self.items.pop(0) #O(n)

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

'''回文词判定 
    1.先将需要判定的词从队尾加如deque
    2.再从两点同时移除字符判定是否相同 知道deque中剩下0个或1个字符'''

def backToWord(str):
    simdeque=Deque()
    for i in str:
        simdeque.addRear(i)
        stillEqual=True
    while simdeque.size()>1:
        if simdeque.removeFront() != simdeque.removeRear():
            stillEqual = False
    return stillEqual

if __name__ == '__main__':
    print(backToWord('radar'))