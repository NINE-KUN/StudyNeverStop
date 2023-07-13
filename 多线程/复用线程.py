"""多线程介绍"""
"""代码的运行是靠拥有调用栈的线程。如果有多个调用栈，CPU就可以在这多个栈上同时或交替运行函数了。根据同时还是交替运行，可以总结多线程的优点：

场景	优点
多线程同时并行，能平衡任务的公平性，也能减少任务的执行总用时。
多线程交替运行，能平衡任务间的公平性，不一定减少任务的执行总用时。
如果有I/O bound任务，多线程能减少总用时；
但如果都是CPU bound任务，多线程不仅不能减少总用时，
反而会由于公平性，让每个用户都较晚才能拿到结果
"""

"""复用线程"""

"""有些小伙伴可能说，每次在拿到结果后，线程不是都会结束么，哪里还有复用线程的机会？
一个线程的调用栈为空后，确实会导致线程被销毁。
让线程一直存在的方法在于让线程的调用栈永不为空，也就是让线程运行的函数具有while True的循环语句，这样的话该函数永远不会被执行完，调用栈也永不为空。
又有小伙伴可能说，如果让线程一直执行有while True的函数，那线程还怎么运行其他函数呢？
最佳实践就是在while True的代码块里，使用队列queue获取外界输入的函数和参数，
从而能在while True的循环体里执行其他函数。

由此，复用线程的框架如下所示：
自定义ReuseThread类继承标准库的Thread，重写__init__()函数只为新增queue来存放新的函数及参数；
重写run()函数让线程运行起来后永不关闭、且能调用新加入queue的函数；
新增add_new_task()函数让外界线程访问，为执行run()函数的线程新增函数。
"""
import threading
import queue


class ReuseThread(threading.Thread):
    def __init__(self):
        super().__init__()  # 使用父类Thread的初始化函数
        self.queue = queue.Queue()  # 用队列queue新增其他函数
        self.daemon = True  # 设置父类的全局变量daemon为true，说明该线程为守护线程
        # 如果进程中只有守护线程在运行，那么进程会结束，所有守护线程也会关闭
        """守护线程： 守护线程指当如果进程中只有守护线程，那么进程会销毁所有线程，然后进程自己也退出
        默认不设置的情况下是没有守护线程的，主线程执行完毕后，会等待子线程全部执行完毕，才会关闭进程。
        
        比如 主线程循环执行10次 子线程死循环设置为守护线程 设置方式有两种  
        1.threading.Thread(target="方法",daemon(是否为守护线程)=True)
        2.线程对象.setDaemon(True)
        当子线程没有设置守护线程 主线程执行结束后 子线程会一直执行
        当子线程设置了守护线程 当主线程循环十次执行结束后 会强制关闭进程 并销毁所有线程 无论子线程是否执行完毕
        
        除了守护线程还有一种方式将 主线程执行结束后 关闭进程 就是用 join()"""

    def run(self):  # 线程一旦被处理器运行，会自动调用run()方法
        while True:  # 让该线程执行的函数不停止，即让调用栈不为空，从而线程不被销毁
            func, args, kwargs = self.queue.get()  # 获取函数、参数来执行
            print('Hook 1: %s' % threading.current_thread().name)  # 看是哪个线程在执行该行代码
            func(*args, **kwargs)
            self.queue.task_done()  # 告知队列取出的任务已完成
            # self.queue.task_done() 用于告诉self.queue.join()该任务已完成

    def add_new_task(self, func, *args, **kwargs):  # 外界线程访问这个函数为执行run方法的线程新增函数
        print('Hook 2: %s' % threading.current_thread().name)  # 看是哪个线程在执行该行代码
        self.queue.put((func, args, kwargs))  # 在队列queue里新增函数、参数



    """让主线程阻塞是为了让主线程等待复用线程执行完函数。不然主线程一结束，身为守护线程的复用线程也会自动销毁，导致函数不会执行完。
    然而主线程调用t.join()方法会让主线程永久阻塞，如果不重写join()而在后续加上t.join()和 print('end')这两行，会发现print('end')永远不会被执行。
    什么原因？
    Thread类自带的.join()方法会阻塞调用它的线程，直至run()方法结束。由于复用线程的run()方法永远不会结束，那么被阻塞的线程会一直阻塞下去。
    怎么解决？
    重写join()方法，自己设定阻塞解除的条件。
    如果线程t执行完了队列queue的所有函数，那就应该让主线程解除阻塞。
    这点可以用queue自带的join()方法。调用queue.join()的线程，都会被阻塞，直到queue中所有任务执行完为止。在ReuseThread类里如下重写join()。
    """

    # 外界线程通过这个函数让外界线程阻塞，等待queue的任务都完成后，外界线程才能被处理器执行。
    def join(self):
        print('Hook 3: %s' % threading.current_thread().name)  # 看是哪个线程在执行该行代码
        self.queue.join()  # 由self.queue.task_done()告诉self.queue.join()是不是所有入队的任务都完成了。


# 要给可复用的线程新增的函数
def func(name):
    print('Hook 4: %s' % threading.current_thread().name)  # 看是哪个线程在执行该行代码
    print(name)


if __name__ == '__main__':
    print('Hook 5: %s' % threading.current_thread().name)  # 看是哪个线程在执行该行代码
    t = ReuseThread()
    t.start()
    t.add_new_task(func, '任务 1')
    t.add_new_task(func, '任务 2')
    t.join()

"""首先，两个任务都被同一个线程执行了（由2个Hook 4都对应Thread-1看出来，而Hook 4安插在func函数中）。
其次，只有Hook 1和Hook 4安插的函数是由线程t执行（包括run()函数和func()函数），其他Hook安插的函数都由主线程MainThread执行（包括add_new_task(),join()）。
最后，python进程会自动退出，这是由于我们把复用线程设置为了守护线程
"""


"""整体逻辑
    主线程  依次实例化对象 调用add_new_task()"""