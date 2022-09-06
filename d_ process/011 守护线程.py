from threading import Thread
import time


def run(name):
    print('%s is running' % name)
    time.sleep(3)
    print('%s is over' % name)


if __name__ == '__main__':
    t = Thread(target=run, args=('jason',))
    t.daemon = True
    t.start()
    print('主')
'''
主线程的结束意味着进程的运行结束
主线程必须等待其他非守护线程的结束才能结束

子线程运行中需要用到进程中的数据,主线程一旦结束,那么资源也将销毁
'''
