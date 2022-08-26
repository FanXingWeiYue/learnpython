# 叠加多个装饰器的加载、运行顺序
def deco1(func):
    def wrapper1(*args, **kwargs):
        print("正在运行====>deco1.wrapper1")
        res = func(*args, **kwargs)
        print("结束运行====>deco1.wrapper1")
        return res

    return wrapper1


def deco2(func):
    def wrapper2(*args, **kwargs):
        print("正在运行====>deco2.wrapper2")
        res = func(*args, **kwargs)
        print("结束运行====>deco2.wrapper2")
        return res

    return wrapper2


def deco3(x):
    def outter3(func):
        def wrapper3(*args, **kwargs):
            print("正在运行====>deco3.wrapper3")
            res = func(*args, **kwargs)
            print("结束运行====>deco3.wrapper3")
            return res

        return wrapper3

    return outter3


# 加载顺序自下而上
@deco1  # index=deco1(wrapper2的内存地址)     ===> index=wrapper1的内存地址
@deco2  # index=deco1(wrapper2的内存地址)     ===> index=wrapper2的内存地址
@deco3(111)  # ===> outter3 ===> index=outter3(index的内存地址)     ===> index=wrapper3的内存地址
def index(x, y):
    print("from index {} {}".format(x, y))


# 执行顺序自上而下 即wrapper1->wrapper2->wrapper3
index("aaa", "bbb")
