import time
from functools import wraps


def index(name, age):
    print("他的姓名:{}".format(name))
    print("他的年龄:{}".format(age))
    return 123


# 装饰器
def outter(func):
    @wraps(func)  # 将原函数的属性赋值给wrapper函数
    def wrapper(*args, **kwargs):
        start = time.time()
        time.sleep(1)
        print("outter装饰器")
        res = func(*args, **kwargs)
        stop = time.time()
        print(stop - start, "outter装饰器")
        return res

    return wrapper


# index = outter(index)
# res = index("张三", 27)
# print(res)


# 在被装饰对象正上方，单独写一行装饰器名字
@outter  # home=outter(home)
def home(name):
    print("welcome {} to home page".format(name))


home("liaojiao")


# 由于语法糖@的限制，outter函数只能有一个参数，并且该参数只用来接收被装饰对象的内存地址
@outter
def home(name):
    print("welcome {} to home page".format(name))


home("liaojiao")


# 无参装饰器模板
def outter(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return res

    return wrapper


# 有参装饰器模板
def deco(x, y, z):
    def outter(func):
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            return res

        return wrapper

    return outter
