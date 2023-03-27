import time


def timer(func, *args, **kwargs):
    start_time = time.time()
    result = func()
    end_time = time.time()
    work_time = round(end_time - start_time, 4)
    print(f'Время работы программы: {work_time}')
    return result


def hard_func():
    return [x ** 2 ** x for x in range(22)]


print(timer(hard_func))
