li = [str(i) for i in range(10)]
li.append(" ")
print(li)
with open("a.py", encoding="utf-8") as f:
    for str in f:
        for i in str:
            if i in li:
                str = str[1:len(str)]
            else:
                with open("c.py", mode="a+", encoding="utf-8") as writer:
                    writer.write(str)
                break
