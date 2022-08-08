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


def money(num):
    dx1 = ["零", "壹", "贰", "叁", "肆", "伍", "陆", "柒", "捌", "玖"]
    dx2 = ["元", "拾", "佰", "仟", "万", "亿"]
    dx3 = ["角", "分", "零", "整"]
    dxnum = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    s = Stock()
    strnum = str(num)
    splst = strnum.split('.')
    index = 0
    findex=0
    for i in splst[0]:
        index += 1
        idx = dxnum.index(i)
        s.push(dx1[idx])
        if idx != 0:
            s.push(dx2[len(splst[0])-index])
    if len(splst) >1:
        for j in splst[1]:
            fidx=dxnum.index(j)
            s.push(dx1[fidx])
            if fidx != 0:
                s.push(dx3[findex])
            findex += 1
    a="".join(str(s.items))
    b=set(a)
    print(a)
if __name__ == '__main__':
    money('1005')


