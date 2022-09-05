# 杀死进程
# 判断进程是否存活
# 寻找主进程

from multiprocessing import Process, current_process
import time
import os


def run(name):
    # print('%s is running'%name,current_process().pid)
    print('%s is running' % name, '子进程%s' % os.getpid(), '父进程%s' % os.getppid())
    time.sleep(3)
    print('%s over' % name)


if __name__ == '__main__':
    p = Process(target=run, args=('egon',))
    p.start()
    # p.terminate()  # 杀死当前进程
    # 是告诉操作系统去帮你杀死当前进程，但是需要一定的时间，而代码的运行速度极快
    time.sleep(1)
    print(p.is_alive())  # 判断进程是否存活
    # print('主', current_process().pid)  # 查看主进程的id号
    print('主', os.getpid(), '主主进程:%s' % os.getppid())
