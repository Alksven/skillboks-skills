from typing import Callable, Any


def do_twice(func: Callable) -> Callable:
    """
    Декоратор, который дважды вызывает декорируемую функцию
    :param func: Декорируемая функция
    :return: функция обертка, вызывает func дважды
    """
    def wrapped_func(*args, **kwargs):
        """
        Функция обертка, вызываютщая func дважды
        :param args: Аргументы переданные в функцию func
        :param kwargs: Ключевые слова, переданные в функцию func
        :return: Рузультат вызова функции func
        """
        for i in range(2):
            func(*args, **kwargs)
    return wrapped_func


@do_twice
def greeting(name: str) -> None:
    """
    Функция которая выводит приветствие.
    :param name: Имя которое нужно поприветствовать
    """
    print('Привет, {name}!'.format(name=name))


greeting('Tom')
