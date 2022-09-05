from multiprocessing import Process
import time

# join方法,主进程等待子进程运行结束,才会继续执行主进程
def run(name, i):
    print('%s running' % (name))
    time.sleep(i)
    print('%s over' % name)


if __name__ == '__main__':
    p = Process(target=run, args=('egon', 3))
    p1 = Process(target=run, args=('jason', 4))
    p2 = Process(target=run, args=('tank', 5))
    start_time = time.time()
    # 并行
    p.start()
    p1.start()
    p2.start()
    p.join()
    p1.join()
    p2.join()
    # 串行
    # p.start()
    # p.join()
    # p1.start()
    # p1.join()
    # p2.start()
    # p2.join()

    # 并行
    # p_list=[]
    # for i in range(1,4):
    #     p = Process(target=run, args=('egon', 3))
    #     p.start()
    #     p_list.append(p)
    # for p in p_list:
    #     p.join()
    #
    end_time = time.time()
    print('主进程')
    print(start_time - end_time)
