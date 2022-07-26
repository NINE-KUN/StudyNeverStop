# 用 户 ： 钱坤
# 使 用 人：钱坤
# 目 的：学习 赚钱
# 开发时间：  0:30

# 条件语句

'''
条件表达式 If....Else
语法结构
X If ... Else  Y
如果If条件后 为True 则输出X 否则为Y
'''

Num_1 = int(input('请输入第一个整数'))
Num_2 = int(input('请输入第二个整数'))
'''if Num_1>Num_2:
    print(Num_1, '大于', Num_2)
else:
    print(Num_2, '大于', Num_1)'''
print('----------使用条件表达式表达----------')
print(str(Num_1)+'大于'+str(Num_2) if Num_1 >= Num_2 else str(Num_1)+'小于'+str(Num_2))