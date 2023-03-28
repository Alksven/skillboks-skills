from typing import Callable, Dict

PLUGINS: Dict[str, Callable] = dict()


def registration(func: Callable) -> Callable:
    PLUGINS[func.__name__] = func
    return func


@registration
def say_hello(name: str) -> str:
    return f'Hello {name}'


@registration
def say_goodbye(name: str) -> str:
    return f'Goodbye {name}'


print(PLUGINS)
print(say_hello('TOM'))