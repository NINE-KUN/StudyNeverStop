
'''栈 后进先出LIFO(Last in First out)
      基于数据项保存时间的次序，时间越短离栈顶越近，而时间越长的离栈底越近
      进栈和出栈顺序相反 先进后出'''

'''
抽象数据类型'栈'定义为如下的操作
Stack()创建一个空栈，不包含任何数据
push(item):将item加入栈顶，无返回值
pop():将栈顶数据移除，并返回，栈被修改
peek():“窥视”栈顶数据项，返回栈顶的数据项但不移除，栈不被修改
isEmpty():返回栈是否为空栈
size():返回栈中有多少个数据项
'''
'''通过面向对象定义抽象数据类型栈(ADT Stack)'''
class Stock():
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items==[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)

