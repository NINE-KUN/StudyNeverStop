# 用 户 ： 钱坤
# 使 用 人：钱坤
# 目 的：学习 赚钱
# 开发时间：  15:05
'''try...except...else...finally结构
    如果try块中没有抛出异常，则执行else块，如果try中抛出异常，则执行except块
    finally块无论是否发生异常都会被执行，能常用来释放try块中申请的资源
'''
try:
    a = int(input('请输入第一个整数'))
    b = int(input('请输入第二个整数'))
    result = a / b
except ZeroDivisionError:
    print('除数不可以为0')
except ValueError:
    print('除数不可以为字母')
else:
    print('结果为',result)
finally:
    print('谢谢您的使用')
    print('程序结束')





