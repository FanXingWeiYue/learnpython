from threading import Thread, Lock, RLock
import time

'''
Rlock锁 也被称之为递归锁
第一个抢到Rlock锁的人,可以连续使用acquire,release
每acquire一次,锁身上计数加1
每release一次,锁身上计数减1
等锁身上的计数为0时,其他人就可以抢锁
'''
# mutexA = Lock()
# mutexB = Lock()
mutexA = mutexB = RLock()


class MyThead(Thread):
    def run(self):  # 创建线程时,会自动执行run方法
        self.func1()
        self.func2()

    def func1(self):
        mutexA.acquire()
        print('%s 抢到了A锁' % self.name)
        mutexB.acquire()
        print('%s 抢到了B锁' % self.name)
        mutexB.release()
        print('%s 释放了B锁' % self.name)
        mutexA.release()
        print('%s 释放了A锁' % self.name)

    def func2(self):
        mutexB.acquire()
        print('%s 抢到了B锁' % self.name)
        time.sleep(1)
        mutexA.acquire()
        print('%s 抢到了A锁' % self.name)
        mutexA.release()
        print('%s 释放了A锁' % self.name)
        mutexB.release()
        print('%s 释放了B锁' % self.name)


for i in range(10):
    p = MyThead()
    p.start()

# 自己千万不要轻易的处理锁的问题
