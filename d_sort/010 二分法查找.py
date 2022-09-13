li = [1, 4, 435, 3, 5, 43, 34, 385, 345, 415, 343, 54, 7, 64, 643, 63]
li = sorted(li)
print(li)


def binary_search(find_num, li, i):
    i = i + 1
    mid_val = li[int(len(li) / 2)]
    if find_num > mid_val:
        li = li[int(len(li) / 2) + 1:len(li)]
        binary_search(find_num, li, i)
    elif find_num < mid_val:
        li = li[0:int(len(li) / 2)]
        binary_search(find_num, li, i)
    else:
        print("find it,found times: {}".format(i))


if __name__ == '__main__':
    i = binary_search(54, li, 0)
