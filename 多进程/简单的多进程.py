import multiprocessing
from multiprocessing import Process, Queue

# multiprocessing 进程包

# 简单的多进程
# def add(queue, num):
#     ret = 1
#     for i in range(1, num):
#         ret = ret + i
#     queue.put(ret)
#
#
# if __name__ == '__main__':
#     q = Queue()
#     ps = []
#     ps.append(Process(target=add, args=(q, 10)))
#     ps.append(Process(target=add, args=(q, 10)))
#
#     for p in ps:
#         p.start()
#         print(q.get())
#         # p.join()

'''
1、导入进程包
    import multiprocessing
    
2、通过进程类创建进程对象
    进程对象 = multiprocessing.Process(target=*)
    此处target的值可以是函数名称 
    args使用方式
    进程对象 = multiprocessing.Process(target=*,args=(*,))
    此处注意，若只有一个元素，那个逗号也是不可以省略的。
    kwargs使用方式
    进程对象 = multiprocessing.Process(target=*,kwargs={"变量名": 变量值})

3、启动进程执行任务
    进程对象.start()
'''
# 吃饭喝汤多进程实现 边吃饭边喝汤
import time

def drink():
    for i in range(3):
        print('喝汤')
        time.sleep(1)
def eat():
    for i in range(3):
        print('吃饭')
        time.sleep(1)

if __name__ == '__main__':
    #target: 指定函数名
    drink_process=multiprocessing.Process(target=drink)
    eat_process=multiprocessing.Process(target=eat)

    drink_process.start()
    eat_process.start()