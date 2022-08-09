class Deque():
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items==[]
    def addRear(self,item):
        self.items.insert(0,item)
    def addFront(self,item):
        self.items.append(item)
    def removeRear(self):
        return self.items.pop(0)
    def removeFront(self):
        return self.items.pop()
    def size(self):
        return len(self.items)

def a(namelst):
    simque=Deque()
    for i in namelst:
        simque.addFront(i)
    while simque.size()>1:
        if simque.removeFront()!=simque.removeRear():
            return False
    return True
if __name__ == '__main__':
    print(a('abdba'))

