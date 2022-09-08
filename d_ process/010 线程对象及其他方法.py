from threading import Thread, current_thread, active_count
import os
import time


def task(name, i):
    print('%s is running' % name)
    print('子{}: {}'.format(current_thread().getName(), current_thread().ident))
    print('子进程:%s' % os.getpid())

    time.sleep(i)
    print('%s is over' % name)


# 开线程不用写在if __name__ == '__main__':中,但是习惯还是写在__main__代码中
if __name__ == '__main__':
    t = Thread(target=task, args=('jason', 1))
    t1 = Thread(target=task, args=('egon', 3))
    t.start()
    t1.start()
    t1.join()  # 主线程等待子线程运行完毕
    print(active_count())  # 查看当前活跃线程数
