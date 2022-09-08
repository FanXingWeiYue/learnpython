# property的使用

import math


# @property装饰器就是负责把一个方法变成属性调用
class Circle:
    def __init__(self, radius):  # 圆的半径radius
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2  # 计算面积


c = Circle(10)
print(c.radius)
print(c.area)  # 可以向访问数据属性一样去访问area,会触发一个函数的执行,动态计算出一个值


class Person(object):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @name.deleter
    def name(self, value):
        print("不让删除")
        del self.__name


p = Person('zhangsan', 20)
print(p.name)
p.name = "lisi"
print(p.name)
