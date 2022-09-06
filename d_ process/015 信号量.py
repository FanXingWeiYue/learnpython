# 信号量可能在不同领域对应不同的知识点
'''
互斥锁:代表一个坑位
信号量:代表一个公共厕所,有多个坑位
'''
from threading import Semaphore, Thread
import time
import random

sm = Semaphore(4)  # 制造一个有五个坑位的厕所


def task(name):
    sm.acquire()
    print('%s 抢到了坑位' % name)
    time.sleep(random.randint(1, 3))
    sm.release()


if __name__ == '__main__':
    for i in range(20):
        t = Thread(target=task, args=(i,))
        t.start()
