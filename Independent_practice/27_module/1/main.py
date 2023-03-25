def func_2(func, num):
    resul = func(num)
    return resul * resul


def func_1(x):
    return x + 10


print(func_2(func_1, 9))