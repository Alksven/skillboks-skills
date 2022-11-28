def tpl_sort(numbers):

    for i in numbers:
        flag = isinstance(i, int)
        if not flag:
            return numbers

    numbers = sorted(list(numbers))
    return tuple(numbers)


print(tpl_sort((6, 3, -1, 85, 4, 10, -5)))
