import functools
from typing import Callable


def decorator_with_args_for_any_decorator(decorator_to_enhance):
    def decorator_maker(*args, **kwargs):
        def decorator_wrapper(func):
            return decorator_to_enhance(func, *args, **kwargs)
        return decorator_wrapper
    return decorator_maker
@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *dec_args, **dec_kwargs):
    @functools.wraps(func)
    def wrapper(*func_args, **func_kwargs):
        print(f'Переданные арги и кварги в декоратор: ({dec_args, dec_kwargs})')
        return func(*func_args, **func_kwargs)
    return wrapper

@decorated_decorator(100, 'рублей', 200, 'друзей', 9868)
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)

decorated_function("Юзер", 101)