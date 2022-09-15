# 方案一
# start_index：表示起始索引(包含该索引本身)；该参数省略时，表示从对象“端点”开始取值
# end_index：表示终止索引(不包含该索引本身)；该参数省略时，表示一直取到数据”端点“
a = "dshjfkskfd"
print(a[::-1])

# 方案二

print(a[len(a)::-1])

# 方案三
for i in range(len(a) - 1, -1, -1):
    print(a[i], end="")
