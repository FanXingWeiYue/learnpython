# lambda表达式配合sorted函数使用，对列表进行排序
data = [472, 34, 5, 24, 342]
datas_sort = sorted(data, key=lambda x: x, reverse=False)
print(datas_sort)
