'''匹配括号 是否合法 如（（））
    方法： 先扫描 查看是什么符号 如果是左括号 放入栈顶 继续匹配
    如果是右括号 查看栈是否空了 如果不空 移除栈顶的左括号
    再继续匹配 左括号放入站 右括号则从栈顶移除左括号 如果扫面完所有字符 栈空了 则匹配成功
    如果扫描出右括号 则栈空了 则说明右括号多了 如果扫描完所有 栈还没空说明左括号多了'''


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


def parChecker(symbolString):
    s = Stock()
    balance = True
    index = 0
    while index < len(symbolString) and balance:
        symbol = symbolString[index]
        if symbol == '([{':
            s.push(symbol)
        else:
            if s.isEmpty():
                balance = False
            else:
                top = s.pop()
                if not match(top, symbol):
                    balance = False
        index = index + 1
    if balance and s.isEmpty():
        return True
    else:
        return False


def match(open, close):
    open = '([{'
    close = ')]}'
    return open.index(open) == close.index(close)


print(parChecker('((()))'))
print(parChecker('(()))'))
