# 用 户 ： 钱坤
# 使 用 人：钱坤
# 目 的：学习 赚钱
# 开发时间：  14:19

#变量的赋值操作
class CPU:
    pass
class Disk:
    pass
class Computer:
    def __init__(self,cpu,disk):
        self.cpu=cpu
        self.disk=disk
#(1)变量的赋值
cpu1=CPU() #创建CPU类的实例
cpu2=cpu1 #赋值给变量
print(cpu1,id(cpu1))
print(cpu2,id(cpu2))

# 类的浅拷贝
''' Python拷贝一般都是浅拷贝，拷贝时，对象包含的子对象内容部拷贝
    因此，源对象与拷贝对象会引用同一个子对象
'''
print('-------------------------------------------')
disk=Disk() #创建一个硬盘类对象
computer=Computer(cpu1,disk) #创建一个计算机类对象
#浅拷贝
import  copy
computer2=copy.copy(computer)
print(computer,computer.cpu,computer.disk)
print(computer2,computer2.cpu,computer2.disk)

'''深拷贝：
     使用copy模块的deepcopy函数，递归拷贝对象中包含的子对象，源对象和拷贝对象所有的子对象也不同
'''
print('----------------------------------------')
computer3=copy.deepcopy(computer)
print(computer,computer.cpu,computer.disk)
print(computer3,computer3.cpu,computer3.disk)