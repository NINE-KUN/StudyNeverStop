# 用 户 ： 钱坤
# 使 用 人：钱坤
# 目 的：学习 赚钱
# 开发时间：  11:04

#函数的定义
def fun(num):
    odd=[] # 奇数
    even=[] # 偶数
    for i in num:
        if i%2:
            # 0的bool类型为False 非0数的bool类型为True
            # 当一个数 与2 的余数不为0时 则bool类型为True 说明该数为奇数 否则为偶数
            odd.append(i)
        else:
            even.append(i)
    return odd,even

# 函数的调用
lst=[10,29,34,23,44,53,55]
print(fun(lst))

'''
函数的返回值
   1.如果函数没有返回值【函数执行完毕后，不需要给调用处提供数据】return可以省略不写
   2.函数的返回值，如果是1个，直接返回原类型
   3.函数的返回值，如果是多个，返回的结果为元组
'''

# 1.如果函数没有返回值【函数执行完毕后，不需要给调用处提供数据】return可以省略不写
def fun1():
    print('hello')
    #return
fun1()

# 2.函数的返回值，如果是1个，直接返回原类型
def fun2():
    return 'hello'
res=fun2()
print(res)

#3.函数的返回值，如果是多个，返回的结果为元组
def fun3():
    return'hello','world'
print(fun3())