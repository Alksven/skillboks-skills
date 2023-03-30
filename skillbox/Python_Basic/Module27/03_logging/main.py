from typing import Callable
import random
import functools
from datetime import datetime


def test_logging(func: Callable) -> Callable:
    """
    Декоратор который записывает ошибки любой декорируемой функции.
    :param func: Декорируемая функция
    :return: Функция обёртка которая проверяет и записывает ошибки любой функции в файл function_errors.log.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Callable:
        """
        Функция обёртка которая проверяет и записывает ошибки любой функции в файл function_errors.log.
        :param args: Аргументы переданные в функцию func
        :param kwargs: Ключевые слова, переданные в функцию func
        :return: Результат вызова функции func
        """
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            print(e)
            data = datetime.now().date()
            time = datetime.now().time()
            with open('function_errors.log', 'a') as error:
                error.write(f'{data} {time} {e}\n')
    return wrapper



@test_logging
def say_goodbye(name: str) -> str:
    """
    Функция которая прощаетя с пользователем
    :param name: Имя пользователя
    :return: Строку с именем пользователя
    """
    return f'Goodbye {name}'

@test_logging
def hard_func(num: int) -> list[int]:
    """
    Функция которая создает список из квадратов от 1 до num
    :param num: Крайнее число в вычислении
    :return: список с квадратами чисел
    """
    return [x ** 2 for x in range(1, num + 1)]

@test_logging
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


print(say_goodbye.__name__, say_goodbye.__doc__)
print(hard_func.__name__, hard_func.__doc__)
print(password_generator.__name__, password_generator.__doc__)