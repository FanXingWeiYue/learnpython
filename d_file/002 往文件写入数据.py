# a+模式: a表示追加，+表示如果文件不存在，将创建一个新文件
with open("../new.txt", mode="a+", encoding="utf-8") as writer:
    writer.write("hello,你好！")
