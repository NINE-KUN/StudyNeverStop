# 用 户 ： 钱坤
# 使 用 人：钱坤
# 目 的：学习 赚钱
# 开发时间：  13:49

'''异常处理机制'''
''' 被动掉坑解决机制
      python提供了异常处理机制，可以在异常出现时及时捕获，然后内部“消化”，让程序继续运行
      try：
        可能出现异常的代码
      except  异常类型:
        处理异常的代码
      
    多个except结构
      捕获异常的顺序按照先子类后父类的顺序，为避免遗漏可能出现的异常，可以在最后增加BaseException
      try：
        可能出现异常的代码
      except  Exception1:
        处理异常的代码
      except  Exception2:
        处理异常的代码
      except  Exception3:
        处理异常的代码
      except  BaseException:
        处理异常的代码
'''
try:
    n1=int(input('请输入一个整数'))
    n2=int(input('请输入另一个整数'))
    result=n1/n2
    print('结果为',result) # 由于人为输入可能会输入字母或0
except ZeroDivisionError:
    print('除数不可以为0')
except ValueError:
    print('除数不可以为字母')
except BaseException as e:
    print(e)