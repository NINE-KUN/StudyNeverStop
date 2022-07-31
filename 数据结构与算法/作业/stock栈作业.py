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

'''括号判断'''
def parChecker(symbolString):
    s = Stock()
    balance = True
    index = 0
    while index < (len(symbolString)) and balance:
        symbol = symbolString[index]
        if symbol in "({[":
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
    open = '{[('
    close = ')]}'
    return open.index(open) == close.index(close)


if __name__ == '__main__':
    print(parChecker('{[()]}'))

'''判断字符串 相同的字母就消除 比如aabbcdd 结果返回c
    原理 判断是否为空栈 是空栈便将循环的字母 入栈与下一个字母比较 相同 从栈删除 不相同就将第二个字母入栈 最后输出栈内所有字母(通过join 加入到空字符串 )'''
def parChecker1(symbolString1):
    st = Stock()
    for res in symbolString1:
        if not st.isEmpty() and res == st.peek():
            st.pop()
        else:
            st.push(res)
    if st.isEmpty():
        print('None')
    else:
        print("".join(str(st.items)))


'''洗碗工小明碰上了一位强迫症老板老王，餐厅一共就10只盘子，老板给仔细编上了0～9等10个号码，并要求小明按照从0到9的编号来洗盘子，当然，每洗好一只盘子，就必须得整齐叠放起来。
小明洗盘子期间，经常就有顾客来取盘子，当然每位顾客只能从盘子堆最上面取1只盘子离开。
老王在收银台仔细地记录了顾客依次取到盘子的编号，比如“1043257689”，这样他就能判断小明是不是遵照命令按照0123456789的次序来洗盘子了。


输入
长度为10的字符串，其中只包含0～9的数字，且不重复，代表顾客依次取到的盘子编号
输出
字符串：Yes或者No，表示遵照次序洗盘子，或者没有遵照次序洗盘子
'''

def parChecker2(s):
    st=Stock()
    n=0
    i=0
    while i<10 and i<10:
        k=int(s[i])
        if n<=k:
            for m in range(n,k+1):
                st.push(m)
            n=k+1
        while not st.isEmpty() and st.peek()==int(s[i]):
            m=st.pop()
            i+=1
    if st.isEmpty():
        print("yes")
    else:
        print("no")


if __name__ == '__main__':
    parChecker1('aabccbd')
    parChecker2('1043257689')