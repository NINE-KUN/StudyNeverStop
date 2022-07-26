# 用 户 ： 钱坤
# 使 用 人：钱坤
# 目 的：学习 赚钱
# 开发时间：  17:13
'''
输出一个三行四列的矩形
'''
for y in range(1,4):
    for x in range(1,5):
        print('*',end='\t')
    print()
'''
输出一个直角三角形
'''
for Y in range(1,10):
    for X in range(1,Y+1):
        print(X,'*',Y,'=',X*Y, end='\t')
    print()

