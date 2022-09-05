'''
生产者:制造/生产数据
消费者:处理/消费数据
例子:做包子,卖包子
    供大于求
    供不应求
    供需问题
生产者消费者模型能解决消费者将队列中的值取完后,会自动结束进程,不会在原地等待
JoinableQueue能够被等待的队列
'''
from multiprocessing import Process, Queue, JoinableQueue
import random
import time


def producer(name, food, q):
    for i in range(10):
        data = '%s生产了%s %s' % (name, food, i)
        time.sleep(random.random())
        q.put(data)
        print(data)


def consumer(name, q):
    while True:
        data = q.get()
        # if data == None:break
        print('%s吃了%s' % (name, data))
        time.sleep(random.random())
        q.task_done()


if __name__ == '__main__':
    q = JoinableQueue()
    p = Process(target=producer, args=('jason', '鸡', q))
    p1 = Process(target=producer, args=('egon', '馒头', q))
    c = Process(target=consumer, args=('tank', q))
    c1 = Process(target=consumer, args=('jerry', q))
    p.start()
    p1.start()
    c.daemon = True
    c1.daemon = True
    c.start()
    c1.start()
    p.join()
    p1.join()  # 生产者确确实实生产结束
    q.join()  # 等待队列中的值全部取完
    print('zhu')

'''
q.task_done()和q.join()是放在一起使用的
在JoinableQueue内部中有个机制,在队列中放入一个值,就会+1,task_done之后就会减一,直到真正取完时
'''
