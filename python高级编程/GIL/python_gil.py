#全局解释器锁
'''python中一个线程对应于C语言中得一个线程，
gil使得同一时刻只有一个线程运行在一个cpu上执行字节码
无法将多个线程映射到多个cpu上 (无法体现多核得优势)所以并发很受限'''

'''gil会根据执行的字节码行数以及时间片释放gil 还会在遇到io操作的时候主动释放'''
# #字节码演示
# import dis
# def add(a): #函数变成字节码得流程(反编译)
#     a =a+1
#     return a
# print(dis.dis(add))

total = 0
def add():
    global total
    for i in range(1000000):
        total += 1

def desc():
    global total
    for i in range(1000000):
        total -= 1

import threading
thread11=threading.Thread(target=add)
thread22=threading.Thread(target=desc)

thread11.start()
thread22.start()

thread11.join()
thread22.join()

print(total)