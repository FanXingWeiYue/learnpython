# 如何得到自定义的迭代器
# 在函数内一旦存在yield关键字，调用函数并不会执行函数体代码，会返回一个生成器对象
# 生成器即自定义的迭代器
def func():
    print("第一次")
    print("第一次")
    yield 1
    print("第二次")
    yield 2
    print("第三次")
    yield 3


g = func()
# 会触发函数体代码的运行，然后遇到yeild停下来，将yeild后的值当作本次调用的结果返回
g.__next__()
