# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。


"""题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
程序分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去 掉不满足条件的排列。
程序源代码："""

def text1():
    for i in range(1,5):
        for j in range(1,5):
            for k in range(1,5):
                if(i != j)and(i != k)and(j != k):
                    print(i,j,k)


"""题目：输入三个整数x,y,z，请把这三个数由小到大输出。
程序分析：我们想办法把最小的数放到x上，先将x与y进行比较，如果x>y则将x与y的值进行交换，
然后再用x与z进行比较，如果x>z则将x与z的值进行交换，这样能使x最小"""
def text2():
    lst=[]
    for i in range(3):
        x=int(input("请输入数字:\n"))
        lst.append(x)
    lst.sort()
    print(lst)

"""题目：斐波那契数列。
程序分析：斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。
在数学上，费波那契数列是以递归的方法来定义："""
def text3(n):
        if n == 1:
            return [1]
        if n == 2:
            return [1, 1]
        lst = [1, 1]
        for i in range(2, n):
            lst.append(lst[-1] + lst[-2])
        return lst
# 输出前 10 个斐波那契数列
print(text3(10))
def text3_1(n):
        a, b = 1, 1
        for i in range(n-1): #因为 a=1,b=1 所以n-1 循环9次
            a, b = b, a + b
        return a
# 输出了第10个斐波那契数列
print('yy',text3_1(10))
print(list(range(10)))
print(list(range(9)))

"""题目：将一个列表的数据复制到另一个列表中。
程序分析：使用列表[:]。"""
def text4():
    a = [1, 2, 3]
    b = a[:]
    c = a
    print(b)
    print(c)
text4()

"""题目：输出 9*9 乘法口诀表。
程序分析：分行与列考虑，共9行9列，i控制行，j控制列。"""
def text5():
    for i in range(1,10):
        print()
        for j in range(1,i+1):
            print("%d*%d=%d  " % (i,j,i*j),end="")
text5()
