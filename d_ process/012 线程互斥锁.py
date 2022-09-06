from threading import Thread, Lock
import time

n = 100


def run(mutex):
    global n
    mutex.acquire()
    num = n
    time.sleep(0.1)
    n = num - 1
    mutex.release()


if __name__ == '__main__':
    l = []
    mutex = Lock()
    for i in range(100):
        t = Thread(target=run, args=(mutex,))
        t.start()
        l.append(t)

    for i in l:
        i.join()

    print(n)
