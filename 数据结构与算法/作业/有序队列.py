"""
    实现一个基数排序算法，用于10进制的正整数从小到大的排序。
    思路是保持10个队列(队列0、队列1......队列9、队列main)，开始，所有的数都在main队列，没有排序。
    第一趟将所有的数根据其10进制个位(0~9)，放入相应的队列0~9，全放好后，按照FIFO的顺序，将每个队列的数合并排到main队列。
    第二趟再从main队列队首取数，根据其十位的数值，放入相应队列0~9，全放好后，仍然按照FIFO的顺序，将每个队列的数合并排到main队列。
    第三趟放百位，再合并；第四趟放千位，再合并。
    直到最多的位数放完，合并完，这样main队列里就是排好序的数列了。
"""


class Queue():
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)


class Queue1(Queue):
    def __init__(self):
        self.items = []


def fun(mylist):
    # 全部入队main
    main = Queue()
    for item in mylist:
        main.enqueue(item)
    # 找最大数，以及位数
    d = len(str(max(mylist)))
    dstr = "%%0%dd" % d
    #准备10个队列
    nums = [Queue() for _ in range(10)]
    # 进行按位基数排序
    for i in range(-1,-d-1,-1):#一趟下标-1~-d,代表个位的最高位
        while not main.isEmpty():
            n = main.dequeue()
            dn=(dstr %n)[i]#转换成类似"00345[-2],这是倒数第二位"
            nums[int(dn)].enqueue(n)
        for k in range(10):
            while not nums[k].isEmpty():
                main.enqueue(nums[k].dequeue())
    #从main队列导出为列表
    result=[]
    while not main.isEmpty():
        result.append(main.dequeue())
    return result
mylist = eval(input())
print(fun(mylist))
