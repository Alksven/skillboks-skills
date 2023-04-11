import random
from typing import Callable, Any


def callback(num: int) -> Callable:
    """
    callback-функций Срабатывает при условии когда параметр num больше чем первое число поступающее
     в декорируемую функцию
    :param num: число для сравнения
    :return: функцию-обертку
    """
    def decorated_func(func: Callable) -> Callable:
        def wrapper(*args: Any, **kwargs: Any) -> Callable:
            """
            Функция-обертка, которая проверяет, num больше или меньше args[0]
            :param args: позиционные аргументы, переданные в декорируемую функцию
            :param kwargs: именованные аргументы, переданные в декорируемую функцию
            :return: результат выполнения декорируемой функции
            """
            result = func(*args, **kwargs)
            if num > args[0]:
                print('Выполнение условия')
            return result
        return wrapper
    return decorated_func


@callback(50)
def bigger(num_1: int, num_2: int) -> None:
    """
    Функция, которая сравнивает два числа
    :param num_1 : Первое число
    :param num_2: Второе число
    """
    if num_1 > num_2:
        print(f'{num_1} больше чем {num_2}')
    else:
        print(f'{num_1} меньше чем {num_2}')


num_list = [random.randint(1, 100) for x in range(2)]

bigger(num_list[0], num_list[1])
