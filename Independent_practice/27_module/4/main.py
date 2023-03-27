from typing import Callable, Any
import time


def timer(func: Callable) -> Callable:
    """
    Декоратор, который замеряет время выполнения функции
    :param func: Декорируемая функция
    :return: Функция обертка, замеряющая время выполнения функции func
    """
    def wrapper(*args, **kwargs):
        """
        Функция обертка, замеряющая время выполнения func
        :param args: Аргументы переданные в функцию func
        :param kwargs: Ключевые слова, переданные в функцию func
        :return: Руеультат вызова функции func
        """
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print(f'Время работы программы: {round(end_time - start_time, 4)}')
    return wrapper


@timer
def hard_func():
    """
    Фунция которая создает список от 0 до 14 и возводит каздое число в квадрат
    :return: готовый список вычислений
    """
    return [x ** 2 ** x for x in range(15)]


hard_func()