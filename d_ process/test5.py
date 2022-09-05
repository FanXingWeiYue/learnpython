# 主进程死亡 子进程也跟着死亡
from multiprocessing import Process
import time


def run(name):
    print('%s 正常运行' % name)
    time.sleep(3)
    print('%s 死亡' % name)


if __name__ == '__main__':
    p = Process(target=run, args=('jason',))
    p.daemon = True  # 将该进程设置为守护进程  这一句话必须放在start前面否则报错
    p.start()
    time.sleep(1)
    print('主进程死亡')
