import time, threading

# 新线程执行的代码:
def loop(n):
    print('thread1 %s is running...' % threading.current_thread().name)
    for i in range(n):
        print('thread1 %s >>> %s' % (threading.current_thread().name, i))
        time.sleep(5)
    print('thread1 %s ended.' % threading.current_thread().name)

print('thread1 %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread', args=(10, ))
t.start()
print('thread1 %s ended.' % threading.current_thread().name)

