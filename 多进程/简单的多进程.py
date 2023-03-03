from multiprocessing import Process, Queue


def add(queue, num):
    ret = 1
    for i in range(1, num):
        ret = ret + i
    queue.put(ret)


if __name__ == '__main__':
    q = Queue()
    ps = []
    ps.append(Process(target=add, args=(q, 10)))
    ps.append(Process(target=add, args=(q, 10)))

    for p in ps:
        p.start()
        print(q.get())
        # p.join()
