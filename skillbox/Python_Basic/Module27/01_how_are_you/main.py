from typing import Callable, Any


def how_are_you(func: Callable) -> Callable:
    """
    Декоратор, который перед выполнением любой функции спрашивает "как дела?"
    :param func: Декорируемая функция
    :return: Функция обёртка которая запрашивает как дела.
    """
    def wrapper(*args: Any, **kwargs: Any) -> Callable:
        """
        Функция обёртка которая запрашивает как дела.
        :param args: Аргументы переданные в функцию func
        :param kwargs: Ключевые слова, переданные в функцию func
        :return: Результат вызова функции func
        """
        hay = input('Как дела? ')
        print('А у меня не очень! Ладно, держи свою функцию.')
        resul = func(*args, **kwargs)
        return resul
    return wrapper


@how_are_you
def say_hello(name: str) -> str:
    return f'Hello {name}'

@how_are_you
def hello():
    print('hello')


@how_are_you
def say_goodbye(name: str) -> str:
    return f'Goodbye {name}'




print(say_goodbye(name='Игорь'))
hello()






