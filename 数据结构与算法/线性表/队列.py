import random


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


'''热土都问题(约瑟夫问题) '''


def hotPotato(namelist, num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)
    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())
        simqueue.dequeue()
    return simqueue.dequeue()


if __name__ == '__main__':
    print(hotPotato(['嘉锐', '邹涛', '钱坤', '魏万卉', '宝音', '任子楠'], 7))

'''打印任务
    1.创建打印队列对象
    2.时间按照秒的单位流逝
        按照概率生成打印作业，加入打印队列
        如果打印机空闲，且队列不空，则取出队首作业打印，记录此作业等待时间
        如果打印机忙，则按照打印速度进行1秒打印
        如果当前作业打印完成，则打印机进入空闲
    3.时间用尽，开始统计平均等待时间
    
    涉及到的时间
        作业的等待时间
            生成作业时，记录生成的时间戳
            开始打印时，当前时间减去生成时间
        作业的打印时间
            生成作业时，记录作业的页数
            开始打印时，页数除以答应速度即可'''


# 打印机类
class Printer():
    def __init__(self, ppm):
        self.pagerate = ppm  # 打印速度
        self.currentTask = None  # 打印任务
        self.timeRemaining = 0  # 任务倒计时

    # 打印1秒
    def tick(self):
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    # 打印忙
    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False

    # 打印新作业
    def startNext(self, newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() / self.pagerate * 60  # 打印对象的页数除以速度 因为按分钟计算所以乘以60


# 作业类
class Task():

    def __init__(self, time):
        # 生成时间戳
        self.timestamp = time
        # 打印页数
        self.pages = random.randrange(1, 21)

    # 返回时间戳
    def getStamp(self):
        return self.timestamp

    # 返回打印了多少页
    def getPages(self):
        return self.pages

    # 等待时间
    def waitTime(self, currenttime):
        return currenttime - self.timestamp  # 当前时间-生成时间


# 1/180概率生成作业 新生成打印作业
def newPrintTask():
    num = random.randrange(1, 181)
    if num == 180:
        return True
    else:
        return False


def simulation(numSeconds, pagesPerMinute):  # numSeconds 模拟多长时间 pagesPerMinute打印机打印模式(一分钟多少页)
    labprinter = Printer(pagesPerMinute)  # 生成一个打印机对象
    printQueue = Queue()  # 准备一个打印队列
    waitingtimes = []  # 初始化等待时间

    for currentSecond in range(numSeconds):
        if newPrintTask():  # 生成打印作业
            task = Task(currentSecond)  # 生成task作业对象
            printQueue.enqueue(task)  # 将新生成的作业排入打印队列

        '''打印过程 如果打印不忙并且打印队列还有作业
        将队列的打印任务取出来为nexttask 把等待时间计算出来加入列表
        然后开始打印 打印1秒'''
        if (not labprinter.busy()) and (not printQueue.isEmpty()):
            nexttask = printQueue.dequeue()
            waitingtimes.append(nexttask.waitTime(currentSecond))
            labprinter.startNext(nexttask)

        labprinter.tick()  # 打印1秒
    averageWait = sum(waitingtimes) / len(waitingtimes)  # 统计平均时间
    print('等待 %6.2f 任务没有完成 ' % averageWait, printQueue.size())

if __name__ == '__main__':
    for i in range(10):
        simulation(3600,10) #运行3600秒 每次打印5页
