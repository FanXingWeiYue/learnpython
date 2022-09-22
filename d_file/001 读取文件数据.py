# 文件也是可迭代的,for in循环直接读取文件
for _ in open("../字符编码.txt", encoding="utf-8"):  # 必须要指定编码格式，否则按照windows系统的默认编码格式gbk
    print(_, end="")

# 使用with as语句进行文件操作
with open("../字符编码.txt", encoding="utf-8") as f:
    for _ in f:
        print(_, end="")

# rb模式
with open("../字符编码.txt", mode="rb") as f:  # 注意:这里以二进制模式打开文件，就不需要指定编码模式了，但是下面要进行解码
    print(f.read(100).decode("utf-8"))

# rt模式
with open("../字符编码.txt", mode="rt", encoding="utf-8") as f:
    print(f.read(100))
