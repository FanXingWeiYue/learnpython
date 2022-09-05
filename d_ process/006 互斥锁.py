'''
模拟抢票不加互斥锁的情况下,所有抢票的进程都是并发,操作同一份数据,会造成数据错乱
这个时候必须加锁处理
将并行变成串行
这样会降低进程的执行效率,但会提高数据的安全性

注意:
    1.锁不要轻易使用 容易造成死锁现象
    2.只在处理数据的部分加锁不要再全局加锁

锁必须在主进程中产生,交给子进程去使用
'''
# 模拟抢票
import json
from multiprocessing import Process, Lock
import time

dir="./ticket.json"
def check():
    with open(dir, 'r', encoding='utf-8') as f:
        res = json.load(f)
    if res.get('ticket'):
        print('余票%s' % res.get('ticket'))
        return True
    print('余票不足')


def buy(i):
    with open(dir, 'r', encoding='utf-8') as f:
        res = json.load(f)
    time.sleep(1)
    if not res.get('ticket'):
        print('%s没抢到票' % i)
        return
    res['ticket'] -= 1
    with open(dir, 'w', encoding='utf-8')as f:
        json.dump(res, f)
        f.flush()
    print('%s 抢到票了' % i)


def run(i, mutex):
    res = check()
    if not res:
        return
    mutex.acquire()  # 抢锁  只要有人抢到了锁 其他人必须等待该人释放锁 随机抢
    buy(i)
    mutex.release()  # 释放锁


if __name__ == '__main__':
    mutex = Lock()  # 生成一把锁
    for i in range(10):
        p = Process(target=run, args=(i, mutex))
        p.start()
