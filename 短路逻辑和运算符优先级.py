
'''短路逻辑 从左往右 只有当第一个操作数的值无法确定逻辑运算的结果时
    才对第二个操作数进行求值'''

a=((not 1)or(0 and 1)or(3 and 4)or(5 and 6)or(7 and 8 and 9))
print(a)

'''总结 and or 输出结果 输出的是 决定and or  最终输出结果的那个数据的值 '''
print(3 and 4) # and运算符 当两边真值运算同时为True 则输出True
               # 3真值运算符已经确定为True 所以python输出右边决定 and运算结果的 数据的值
print(3 or 4) # or运算符
              # 3真值运算符已经确定为True 所以python输出决定 or运算结果的 数据的值

'''运算符优先级'''