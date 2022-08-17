'''给定一个列表，返回所有数的和'''

'''递归 三定律
    1.递归算法必须有一个基本的结束条件(最小规模问题直接解决)
    2.递归算法必须能改变状态像基本结束条件演进(减小问题规模)
    3.递归算法必须调用自生(解决减小了规模的相同问题)'''

'''我们认识到的求和实际上是由一次一次加法实现的
    加法恰好有两个操作数 想办法将问题规模较大的列表求和
    分解为规模较小而固定的两个数求和'''

'''(1+(3+(5+(7+9))))
    数列的和=首个数+余下数列'''
def listsum(numList):
    if len(numList)==1:
        return numList[0]
    else:
        return numList[0]+listsum(numList[1:])
print(listsum([1,3,5,7,9]))
