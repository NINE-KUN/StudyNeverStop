
class Queue():
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return True
    def enquenue(self,item):#O(n)
        self.items.insert(0,item)
    def dequeue(self):#O(1)
        self.items.pop()
    def size(self):
        return len(self.items)