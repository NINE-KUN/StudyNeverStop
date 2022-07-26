# 用 户 ： 钱坤
# 使 用 人：钱坤
# 目 的：学习 赚钱
# 开发时间：  0:01
# input函数

'''
 作用：接收用户输入的内容

 返回值类型：用户输入值的类型为str
 值得存储：使用=对输入值进行存储
'''

# present = input("钱坤想要什么礼物呢")
# print(present, type(present))


# 练习
# 要求用户录入两个数 并计算两数之和
Number1 = input('请输入一个数字')
Number2 = input('请输入另一个数字')
print(int(Number1)+int(Number2)) # 由于Input输出类型是str类型 需要将str类型通过int()转换为int类型

Number3 = input('请输入一个数字')
Number4 = input('请输入另一个数字')
add = Number3+Number4
add1 = input('请计算两数之和')
add = add1
if add == add1:
  print('恭喜你答对了')
else:
    print('答错了哦')

