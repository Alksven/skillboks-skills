def a(_func=None, *, count=3):
    def b(func):
        def c(*args, **kwargs):
            for i in range(count):
                func(*args, **kwargs)
            return
        return c
    if _func is None:
        return b
    return b(_func)



@a()
def aa(num=3):
    print(3 + num)

aa()