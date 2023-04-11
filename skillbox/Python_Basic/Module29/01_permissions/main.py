import functools
from typing import Callable, Any


def check_permission(user: str) -> Callable:
    """
    Декоратор, который проверяет, имеет ли пользователь необходимые права.

    :param user: имя пользователя
    :return: функцию-обертку
    """
    def check_permission_1(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Callable:
            """
            Функция-обертка, которая проверяет, имеет ли пользователь необходимые права.
            :param args: позиционные аргументы, переданные в декорируемую функцию
            :param kwargs: именованные аргументы, переданные в декорируемую функцию
            :return: результат выполнения декорируемой функции
            """
            if user_permissions[0] == user:
                result = func(*args, **kwargs)
                return result
            else:
                raise PermissionError(f'у пользователя недостаточно прав, чтобы выполнить функцию {func.__name__}')
        return wrapper
    return check_permission_1


user_permissions: list = ['admin']


@check_permission('admin')
def delete_site():
    """
    Функция для удаления сайта. Для успешного выполнения необходимы права администратора.
    """
    print('Удаляем сайт')


@check_permission('user_1')
def add_comment():
    """
    Функция для добавления комментария. Для успешного выполнения необходимы права пользователя user_1.
    """
    print('Добавляем комментарий')

delete_site()
add_comment()