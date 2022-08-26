# 文件也是可迭代的,for in循环直接读取文件
for _ in open("main.py"):
    print(_, end="")
print("----------------------------------------------------------")

with open("main.py") as f:
    for _ in f:
        print(_, end="")
# rb模式
with open("main.py", mode="rb") as f:
    print(f.read(4).decode("utf-8"))
# rt模式
with open("main.py", mode="rt") as f:
    print(f.read(4))
