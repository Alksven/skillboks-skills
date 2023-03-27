from typing import Callable


def vegetables(func: Callable) -> Callable:
    """
    Деоратор который добавляет офощи в бургер
    :param func: Декорируемая функция
    :return: Функция обертка, которая добавляет овощи в бургер
    """
    def wrapper(*args, **kwargs):
        """
        Функция обертка, добавляет овощи в func
        :param args: Аргументы переданные в функцию func
        :param kwargs: Ключевые слова, переданные в функцию func
        :return: Результат вызова функции func
        """
        print('Помидоры')
        func(*args, **kwargs)
        print('салат')
    return wrapper


def bread(func: Callable) -> Callable:
    """
    Деоратор который добавляет булочку в бургер
    :param func: Декорируемая функция
    :return: Функция обертка, которая добавляет булочку в бургер
    """
    def wrapper(*args, **kwargs):
        """
        Функция обертка, добавляет булочку в func
        :param args: Аргументы переданные в функцию func
        :param kwargs: Ключевые слова, переданные в функцию func
        :return: Результат вызова функции func
        """
        print('< / ----------\ >')
        func(*args, **kwargs)
        print('<\______/>')
    return wrapper


@bread
@vegetables
def full_burger(meat: str) -> None:
    """
    Функция, которая добавляет основной ингридиент в бургер
    :param meat: Основной ингридиент
    """
    print(meat)


full_burger('Котлета')