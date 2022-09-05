"""
什么是线程
    进程线程其实都是虚拟单位,都是用来帮助我们形象的描述某种事物

    进程:资源单位
    线程:执行单位
        将内存比如成工厂
        那么进程就相当于是工厂里面的车间
        而你的线程就相当于是车间里面的流水线
    ps:每个进程都自带一个线程,线程才是真正的执行单位,进程只是在线程运行过程中
    提供代码运行所需要的资源


为什么要有线程
    开进程
        1.申请内存空间  耗资源
        2."拷贝代码"    耗资源

    开线程
        一个进程内可以起多个线程,并且线程与线程之间数据是共享的
    ps:开启线程的开销要远远小于开启进程的开销

如何使用线程
"""
# 创建线程的两种方式
from threading import Thread
import time

# def run(name):
#     print('%s is running'%name)
#     time.sleep(3)
#     print('%s is over'%name)
#
#
# if __name__ == '__main__':
#     p = Thread(target=run, args=('jason',))
#     p.start()


'''
使用继承类来创建进程或者线程时,他会自动执行类中的run方法
'''


class MyThread(Thread):
    def __init__(self, name):
        super().__init__()
        # 重写了别人的方法，又不知道别人的方法有啥，你就super调用父类的方法
        self.name = name

    def run(self):
        print('%s is running' % self.name)
        time.sleep(3)
        print('%s is over' % self.name)


if __name__ == '__main__':
    p = MyThread('jason')
    p.start()
