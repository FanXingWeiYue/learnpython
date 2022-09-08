class A:
    x = 1

    @classmethod  # 类方法是给类用的
    def test(cls):
        print(cls.x)


A.test()


class Foo:
    @staticmethod  # 静态方法是类和实例都可以调用
    def spam(x, y, z):
        print(x, y, z)


Foo.spam(1, 2, 3)  # 调用函数应该有几个参数就传几个参数
f1 = Foo()
f1.spam(3, 3, 3)  # 实例也可以使用,但通常静态方法都是给类用的,实例在使用时丧失了自动传值的机制
