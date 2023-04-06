import math
import datetime
import time
import functools


def time_create(cls):
    def wrapper(*args, **kwargs):
        result = cls(*args, **kwargs)
        time = datetime.datetime.now()
        print('Класс создан:', time)
        for i_method in dir(cls):
            if i_method.startswith('__') is False:
                print(i_method)
        return result

    return wrapper


def logging(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as ex:
            print(ex)
    return wrapper


def for_all_methods(decorator):
    @functools.wraps(decorator)
    def decorate(cls):
        for i_method in dir(cls):
            if i_method.startswith('__') is False:
                print()
                cur_method = getattr(cls, i_method)
                decorated_method = decorator(cur_method)
                setattr(cls, i_method, decorated_method)
        return cls
    return decorate



@time_create
@for_all_methods(logging)
class Car:

    def __init__(self, x, y, a):
        self.x = x
        self.y = y
        self.a = math.radians(a)
        self.distance = 0

    def print(self):
        print('print')


    def move(self):
        print('move')

    def turn(self):
        a = 'a' + 3
        print('turn')



car = Car(x=2, y=3, a=5)
car.turn()
car.move()




