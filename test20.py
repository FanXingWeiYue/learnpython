# 一
# 1、类名
class_name = "People"
# 2、类的基类
class_bases = (object,)
# 3、执行类体代码拿到类的名称空间
class_dic = {}
class_body = """
def __init__(self, name, age):
    self.name = name
    self.age = age

def say(self):
    print("{} {}".format(self.name, self.age))
"""
exec(class_body, {}, class_dic)
# 4、调用元类
# class_name:类名、class_bases：基类、class_dic：类的名称空间
People = type(class_name, class_bases, class_dic)
print(People)


# 二、如何自定义元类产生
class Mymeta(type):  # 只有继承了type类才能称之为一个元类，否则就是一个普通的自定义类
    def __call__(self, *args, **kwargs):  # self=<class '__main__.People'>
        # 1、调用__new__产生一个空对象obj
        obj = self.__new__(self)  # 此处的self是类People，必须传参，代表创建一个People的对象obj

        # 2、调用__init__初始化空对象obj
        self.__init__(obj, *args, **kwargs)

        # 在初始化之后，obj.__dict__里就有值了
        obj.__dict__ = {'_%s__%s' % (self.__name__, k): v for k, v in obj.__dict__.items()}
        # 3、返回初始化好的对象obj
        return obj


# People=Mymeta(class_name, class_bases, class_dic)
# 调用Mymeta发生三件事
# 1、先造一个空对象==>People
# 2、调用People这个类内的__init__方法，完成初始化对象的操作
# 3、返回初始化好的对象

class People(object, metaclass=Mymeta):
    school = 'Stanford'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        print('%s says welcome to the Stanford to learn Python' % self.name)


t1 = People('lili', 18)
print(t1.__dict__)  # {'_People__name': 'lili', '_People__age': 18}
