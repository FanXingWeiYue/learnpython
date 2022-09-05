# 创建进程的两种方式
# 创建进程第一种方法
from multiprocessing import Process
import time


def run(name):
    print('%s running' % name)
    time.sleep(3)
    print('%s over' % name)


# 在windows中创建进程时,他会像导入模块一样加载一遍代码,所以创建子进程时,他不会走if __name__ == '__main__':
# 下面的代码块,解决了无限创建进程的问题
if __name__ == '__main__':
    p = Process(target=run, args=('egon',))  # 创建一个进程对象
    p.start()  # 告诉操作系统创建一个进程
    print('主进程')

'''
p.start()告诉操作系统创建一个进程后
操作系统会去内存中开辟一个空间
然后像导入模块一样将代码放进一个独立的内存中

进程与进程之间是隔离的,无法直接进行交互
我们可以通过一些技术,实现交互
'''

# 创建进程的第二种方法
# 通过继承进程类,创造进程,类似于继承元类
from multiprocessing import Process
import time


class MyProcess(Process):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print('%s is running' % self.name)
        time.sleep(3)
        print('%s is over' % self.name)


if __name__ == '__main__':
    p = MyProcess('json')
    p.start()
    print('主')
