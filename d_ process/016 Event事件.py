from threading import Event, Thread
import time

'''
event事件能实现子线程等待子线程运行结束
join只能主线程等待子线程运行结束
'''

# 先生成一个event对象
e = Event()


def light():
    print('红灯亮')
    time.sleep(2)
    e.set()
    print('绿灯亮')


def car(name):
    print('%s 正在等红灯' % name)
    e.wait()
    print('%s 开始踩油门' % name)


if __name__ == '__main__':

    l = Thread(target=light)
    l.start()
    for i in range(10):
        c = Thread(target=car, args=(i,))
        c.start()
