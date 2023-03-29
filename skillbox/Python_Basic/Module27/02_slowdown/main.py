from typing import Callable, Any
import time


def wait(func: Callable) -> Callable:
    """
    Декоратор, который откладывает выполнение функции
    :param func: Декорируемая функция
    :return: Функция обёртка которая откладывает выполнение функции.
    """
    def wrapper(*args, **kwargs) -> Callable:
        """
        Функция обёртка которая откладывает выполнение функции.
        :param args: Аргументы переданные в функцию func
        :param kwargs: Ключевые слова, переданные в функцию func
        :return: Результат вызова функции func
        """
        time.sleep(2)
        result = func(*args, **kwargs)
        return result
    return wrapper


@wait
def say_goodbye(name: str) -> str:
    return f'Goodbye {name}'


print(say_goodbye(name='Игорь'))