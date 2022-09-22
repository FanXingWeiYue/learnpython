# 1、什么是序列化和反序列化
# 内存中的数据类型--->序列化--->特定的格式（json格式或者pickle格式）
# 内存中的数据类型<---反序列化<---特定的格式（json格式或者pickle格式）

# 2、为何要序列化
# 序列化得到结果==>特定格式的内容有两种用途
# 1、可用于存储==>用于归档
# 2、传输给其他平台使用==>跨平台交互
import pickle

# pickle模块是Python专用的持久化模块，可以持久化包括自定义类在内的各种数据，比较适合Python本身复杂数据的存贮。
#
# 但是持久化后的字串是不可认读的，并且只能用于Python环境，不能用作与其它语言进行数据交换。
#
# 把 Python 对象直接保存到文件里，而不需要先把它们转化为字符串再保存，也不需要用底层的文件访问操作，直接把它们写入到一个二进制文件里。pickle 模块会创建一个 Python 语言专用的二进制格式，不需要使用者考虑任何文件细节，它会帮你完成读写对象操作。用pickle比你打开文件、转换数据格式并写入这样的操作要节省不少代码行。
dic = {"liaojiao": 28, "lixiaogang": 30, "liaohui": 22}
# pickle在dump()和load()读写文件时，要使用rb或wb模式，也就是只接收bytes类型的数据
with open("pickle.txt", mode="wb") as f:
    pickle.dump(dic, f)

with open("pickle.txt", mode="rb") as f:
    dic1 = pickle.load(f)
    print(type(dic1))
    print(dic1)
