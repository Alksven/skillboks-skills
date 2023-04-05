import time


def a(_func=None, *, sec=2):
    def b(func):
        def c(*args, **kwargs):
            print('start')
            time.sleep(sec)
            func(*args, **kwargs)
            return
        return c
    if _func is None:
        return b
    return b(_func)


@a
def aa(num=3):
    print(3 + num)

aa()