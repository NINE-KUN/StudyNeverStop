from threading import Thread, Lock
import time

lock = Lock()#定义锁

def add(num):
    ret = 1
    for i in range(1,num):
        try:
            lock.acquire(True)#加锁 ，返回True
            ret = ret + i
            time.sleep(0.1)
        finally:
            lock.release()#解锁，返回True
        print(ret)

if __name__ == '__main__':
    threads = []
    threads.append(Thread(target=add,args=(20,)))
    threads.append(Thread(target=add,args=(20,)))

    for t in threads:
        t.start()
        #t.join() #阻塞的