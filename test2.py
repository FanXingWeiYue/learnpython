from collections.abc import Iterator, Iterable

iter1 = [i for i in range(5)]
iter2 = (i for i in range(5))
print(isinstance(iter1, Iterable))  # 判断对象是否是可迭代的
print(isinstance(iter1, Iterator))  # 判断对象是否是迭代器对象
print(isinstance(iter2, Iterable))
print(isinstance(iter2, Iterator))
print(dir(iter2))
