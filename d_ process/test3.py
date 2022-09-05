from multiprocessing import Process

# 进程之间数据相互隔离
money = 100


def task():
    global money  # 局部修改全局
    money = 666
    print("子进程", money)


if __name__ == '__main__':
    p = Process(target=task)
    p.start()
    p.join()
    print("主进程", money)
