import os
import time
from threading import Thread, Lock

# 线程之间的资源是共享的
money = 100


def task(mutex):
    global money  # 局部修改全局
    mutex.acquire()
    time.sleep(1)
    money = money - 1
    print('PID: %s money: %s' % (os.getpid(), money))
    mutex.release()


if __name__ == '__main__':
    mutex = Lock()
    p_list = []
    for i in range(1, 4):
        p = Thread(target=task, args=(mutex,))
        p.start()
        p_list.append(p)
    for p in p_list:
        p.join()

    print("主进程", money)
