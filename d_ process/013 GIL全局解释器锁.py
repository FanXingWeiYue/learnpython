"""
In CPython, the global interpreter lock, or GIL, is a mutex that prevents multiple
native threads from executing Python bytecodes at once. This lock is necessary mainly
because CPython’s memory management is not thread-safe.
"""
'''
ps:python解释器有很多种,最常见的就是CPython解释器
GIL本质就是一把互斥锁:将并发变成串行牺牲效率保证数据安全
用来阻止同一个进程下的多个线程的同时执行(同一个进程内多个线程无法实现并行,但能并发

GIL的存在就是因为CPython解释器的内存管理不是线程安全的
    为什么不安全呢?
        在Python解释器中有一个垃圾回收机制,那也是一串代码,也是一个进程,
        在并行时,可能会造成一个问题,其他线程变量名还没有赋值时,垃圾回收机制就将值回收了
        就会造成变量名找不到值
        所以需要并发
GIL全局解释器锁是Python中特有的吗?
不是在cpython中才有
    内存管理
    引用计数:值与变量的绑定关系的个数
    标记清除:当内存快要满的时候 会自动停止程序的运行 检测所有的变量与值的绑定关系
    给没有绑定关系的值打上标记，最后一次性清除
    分代回收:(垃圾回收机制也是需要消耗资源的，而正常一个程序的运行内部会使用到很多变量与值
    并且有一部分类似于常量，减少垃圾回收消耗的时间，应该对变量与值的绑定关系做一个分类
    ) 新生代(5S)》》》青春代(10s)》》》老年代(20s)
    垃圾回收机制扫描一定次数发现关系还在，会将该对关系移至下一代
    随着代数的递增 扫描频率是降低的



研究python的多线程是否有用需要分情况讨论
四个任务 计算密集型的 10s
单核情况下
    开线程更省资源
多核情况下
    开进程 10s
    开线程 40s

四个任务 IO密集型的
单核情况下
    开线程更省资源
多核情况下
    开线程更省资源    

'''
# 计算密集型
# from multiprocessing import Process
# from threading import Thread
# import os
# import time
# def work():
#     res = 1
#     for i in range(100000000):
#         res *= i
#
#
# if __name__ == '__main__':
#     l = []
#     print(os.cpu_count())  # 4核
#     start_time = time.time()
#
#     for i in range(4):
#         p = Process(target=work)  # 耗时10.977932214736938秒
#         # p = Thread(target=work)  # 耗时22.046306133270264秒
#         l.append(p)
#         p.start()
#     for i in l:
#         i.join()
#     print(time.time() - start_time)


# IO密集型
from multiprocessing import Process
from threading import Thread
import time
import os


def work():
    time.sleep(3)


if __name__ == '__main__':
    l = []
    print(os.cpu_count())  # 本机4核 本机再算计算密集型就炸了
    start_time = time.time()
    for i in range(400):
        p = Process(target=work)  # 耗时36.039791107177734 大部分时间浪费在开辟内存中间上
        # p = Thread(target=work)  # 耗时3.0542681217193604秒
        l.append(p)
        p.start()
    for p in l:
        p.join()
    print(time.time() - start_time)

'''
pythyon的多线程到底有没有用
需要分情况讨论
在计算密集型上python处于弱势,但在IO密集型上Python还是很强的

我们以后会用到多进程＋多线程配合使用
'''

'''
在开始我们也提到过GIL全局解释器锁本质就是一把互斥锁
    有些人就会认为有了GIL锁之后,我们在处理数据时,就不用加互斥锁了,
    实则不然,GIL全局解释器锁遇到IO时.cpu就会剥夺其使用权限,去执行其他的线程
    我们在处理数据时,就会遇到IO操作(比如网络延迟)所以我们需要使用到普通互斥锁,保证数据安全
'''
