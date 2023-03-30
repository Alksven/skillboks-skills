from typing import Callable, Any
import random
import functools
from datetime import datetime

COUNT = {1: 0}


def counter(func: Callable) -> Callable:
    """
    Декоратор который подсчитывает и выводит в консоль количество запусков функции
    :param func: Декорируемая функция
    :return: Функцию обёртку которая подсчитывает и выводит в консоль количество запусков функции
    """
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Callable:
        """
        Функцию обёртку которая подсчитывает и выводит в консоль количество запусков функции
        :param args: Аргументы переданные в функцию func
        :param kwargs: Ключевые слова, переданные в функцию func
        :return: Результат вызова функции func
        """
        COUNT[1] += 1
        result = func(*args, **kwargs)
        print(f'Функция {func.__name__} выполнилась {COUNT[1]} раз(а)\n')
        return result

    return wrapper


@counter
def password_generator() -> None:
    """
    Функция которая генерирует случайный пароль из 2 символов, используя для этого англ.буквы в верхнем и нижнем
    регистре, цифры, символы.
    """
    little_alpha: str = 'abcdefghijklmnopqrstuvwxyz'
    big_alpha: str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    sym: str = '~!@#$%^&*()_-+={}[]\|:;"<>,.?/'
    num: str = '0123456789'

    time_pas = ''
    for _ in range(5):
        time_pas += little_alpha[random.randint(0, len(little_alpha) - 1)]
        time_pas += big_alpha[random.randint(0, len(big_alpha) - 1)]
        time_pas += sym[random.randint(0, len(sym)) - 1]
        time_pas += num[random.randint(0, len(num) - 1)]
    password_ready = random.sample(time_pas, len(time_pas))
    password_ready = ''.join(password_ready)
    print(password_ready)
    print('Password created')



password_generator()
password_generator()
password_generator()
password_generator()
password_generator()