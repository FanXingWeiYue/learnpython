from multiprocessing import Process, Queue
# 进程间通信ICP机制

def send(q):
    q.put('hello')


def get(q):
    print(q.get())


if __name__ == '__main__':
    q = Queue()
    p = Process(target=send, args=(q,))
    p1 = Process(target=get, args=(q,))
    p.start()
    p1.start()

'''
子进程放数据,主进程获取数据
两个子进程相互放,互相取
'''
