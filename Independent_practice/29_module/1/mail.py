from contextlib import contextmanager
from collections.abc import Iterator
import time

@contextmanager
def timer() -> Iterator:
    start = time.time()
    try:
        yield
    except Exception as ax:
        print('ошибка', ax)
    finally:
        print(time.time() - start)


with timer() as a:
    ab = 4 ** 10
    print(ab)
