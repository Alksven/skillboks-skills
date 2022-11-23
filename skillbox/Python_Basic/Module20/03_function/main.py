def slicer(list, num):
    ready_list = []
    if num not in list:
        return tuple(ready_list)
    elif list.count(num) == 1:
        return list[num - 1:]
    else:
        idx = [x for x, n in enumerate(list) if n == num]
        for i, n in enumerate(list[idx[0]:idx[1] + 1]):
            ready_list.append(n)
    return tuple(ready_list)

# print(slicer((1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10), 2))
