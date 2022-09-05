import os
import time
from threading import Thread, Lock

# 锁必须在主进程中产生,交给子进程去使用
"""
注意:
    1.锁不要轻易使用 容易造成死锁现象
    2.只在处理数据的部分加锁不要再全局加锁
"""
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
