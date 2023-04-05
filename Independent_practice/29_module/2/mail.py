from contextlib import contextmanager
import os


@contextmanager
def in_dir(path):
    cur_path = os.getcwd()
    try:
        os.chdir(path)
    except Exception as ex:
        print(ex)
    try:
        yield
    finally:
        os.chdir(cur_path)


with in_dir('/home'):
    print(os.listdir())

