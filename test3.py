# 1.可变长度的位置参数
# I:*形参名:用来接收溢出的位置实参，溢出的位置实参会被*保存成元组的格式，然后赋值紧跟其后的形参名
#          *后跟的可以是任意名字，但是约定俗成应该是args
def func(x, y, *z):
    print(x, y, z)


func(1, 2, 3, 4, 5, 6)


# II:*可以用在实参中，实参中带*，将*后的值拆分成位置参数
def func(x, y, z):
    print(x, y, z)


func(*[11, 22, 33])


# III:形参与实参中都带*
def func(x, y, *args):
    print(x, y, args)


func(1, 2, *[3, 4, 5, 6])


# 2.可变长度的关键字参数
# I:**形参名:用来接收溢出的位置实参，溢出的位置实参会被**保存成字典的格式，然后赋值紧跟其后的形参名
#           **后跟的可以是任意名字，但是约定俗成应该是kwargs
def func(x, y, **kwargs):
    print(x, y, kwargs)


func(1, y=2, a=3, b=4, c=5, d=6)


# II:**可以用在实参中(**后跟的只能是字典)，实参中带*，将**后的值拆分成关键字参数
def func(x, y, z):
    print(x, y, z)


func(*{'x': 11, 'y': 22, 'z': 33})  # func('x','y','z')
func(**{'x': 11, 'y': 22, 'z': 33})  # func(x=11,y=22,z=33)


# III:形参与实参中都带*
def func(x, y, **kwargs):
    print(x, y, kwargs)


func(**{'y': 22, 'x': 11, 'a': 33, 'b': 44})


# 混用*与**：*args必须在**kwargs之前
def func(x, *args, **kwargs):
    print(args)
    print(kwargs)


func(1, 2, 3, 4, 5, 6, 7, 8, a=1, b=2, c=3)
