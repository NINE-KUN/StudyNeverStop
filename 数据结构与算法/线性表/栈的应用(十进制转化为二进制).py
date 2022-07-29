class Stock():
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):  # O(1)
        self.items.append(item)

    def pop(self):  # O(1)
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

def divideBy2(decNumber):
    remstack=Stock()
    while decNumber>0:
        rem=decNumber%2
        remstack.push(rem)
        decNumber=decNumber//2
    binString=''
    while not remstack.isEmpty():
        binString=binString+str(remstack.pop())
    return binString
print(divideBy2(233))
