import math
import datetime
import time


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


@time_create
class Car:

    def __init__(self, x, y, a):
        self.x = x
        self.y = y
        self.a = math.radians(a)
        self.distance = 0

    def move(self):
        distance_now = float(input(f'Проехал расстояние {self.__class__.__name__}: '))
        self.distance += distance_now
        self.x = self.x + distance_now * math.cos(self.a)
        self.y = self.y + distance_now * math.sin(self.a)
        self.turn()

    def turn(self):
        choice_turn = int(input('Поворот 1 = да / 2 = нет:'))
        if choice_turn == 1:
            self.a = math.radians(int(input('Куда поворачиваем? Лево = 180, Право = 0, Вверх = 90, Вниз = 270: ')))
        else:
            print('Едем дальше!')

    def __str__(self):
        return f'\nПоложение {self.__class__.__name__}: {round(self.x, 1)} : {round(self.y, 1)}\nУгол направления движения: ' \
               f'{round(self.a, 1)}\nПроехал всего расстояния: {self.distance}\n'


car = Car(x=2, y=3, a=5)
time.sleep(2)
car_1 = Car(x=2, y=3, a=5)

