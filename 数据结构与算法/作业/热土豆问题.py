import queue
class Queue():
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return True
    def enquenue(self,item):#O(n)
        self.items.insert(0,item)
    def dequeue(self):#O(1)
        return self.items.pop()
    def size(self):
        return len(self.items)

def hotPotato(namelist,num):
    simqueu=Queue()
    for name in namelist:
        simqueu.enquenue(name)

    while simqueu.size()>1:
        for i in range(num):
            simqueu.enquenue(simqueu.dequeue())
        simqueu.dequeue()
    return simqueu.dequeue()
if __name__ == '__main__':
    print(hotPotato(['邹涛','宝音','钱坤','嘉锐','任子楠','魏万慧'],7))
