from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import os
import time

'''
进程池与线程池

开进程开线程都需要消耗资源，只不过两者比较的情况线程消耗的资源比较少

在计算机能够承受范围之内最大限度的利用计算机


什么是池？
    在保证计算机硬件安全的情况下最大限度的利用计算机
    池其实是降低了程序的运行效率 但是保证了计算机硬件的安全
    (硬件的发展跟不上软件的速度)
'''

# pool = ThreadPoolExecutor()  # 括号内可以传参数指定线程池内的线程个数
# 也可以不穿默认的是计算机cpu个数乘以5

pool = ProcessPoolExecutor()  # 不传,默认参数为cpu个数
'''
池子中创建的进程或者线程创建一次就不会再创建了
至始至终用的都是最初的几个
这样的话节省了反复开辟进程或者线程的资源
'''


def task(n):
    print(n, os.getpid())
    time.sleep(2)
    return n ** 2, n


def call_back(x):
    print(x)
    print('拿到了异步提交任务的返回结果:', x.result())


# if __name__ == '__main__':
#     pool.submit(task, 2)  # 朝线程池/进程池提交任务,异步提交
#     print('zhu')
'''
异步提交任务之后,不等任务的返回结果(异步的结果怎么拿???),直接执行下一行代码
异步回调机制:当异步提交的任务有返回结果之后,会自动触发回调函数的执行
'''

if __name__ == '__main__':
    t_list = []
    for i in range(40):
        # res = pool.submit(task, i)
        res = pool.submit(task, i).add_done_callback(call_back)  # 提交任务的时候 绑定一个回调函数 一旦该任务有结果  立刻执行绑定的回调函数
        # print(res.result())  # 原地等待任务的返回结果,把并行变成串行
        # t_list.append(res)

    # pool.shutdown()  # 关闭池子 等待池子中所有的任务执行完毕之后 才会执行下面的代码
    # for p in t_list:
    #     print('>>>:', p.result())
