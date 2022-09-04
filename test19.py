# 1、什么是内置方法？
# 定义在类的内部，以__开头以__结尾的方法
# 特点：会在某种情况下自动触发执行

# 2、为什么要用内置方法？
# 为了定制化我们的类or对象

# 3、如何使用内置方法
# __str__:
class People:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "{} {}".format(self.name, self.age)


obj = People("liaojiao", 18)
print(obj)


class Foo:

    def __del__(self):
        print('执行我啦')


f1 = Foo()
print('------->')
