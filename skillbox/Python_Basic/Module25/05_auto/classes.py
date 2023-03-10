import math


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


class Bus(Car):

    count_passengers = 0

    def __init__(self, x, y, a):
        super().__init__(x, y, a)
        self.passengers = 0
        self.money = 0

    def move(self):
        distance_now = float(input(f'\nПроехал расстояния: {self.__class__.__name__}? '))
        self.distance += distance_now
        self.x = self.x + distance_now * math.cos(self.a)
        self.y = self.y + distance_now * math.sin(self.a)
        self.turn()
        self.passengers_enter()

    def passengers_enter(self):
        now_passengers = int(input('Вошло пассажиров: '))
        self.passengers += now_passengers
        Bus.count_passengers += now_passengers
        self.money += now_passengers * 50
        self.passengers_exit()

    def passengers_exit(self):
        count_passengers = int(input('Вышло пассажиров: '))
        self.passengers -= count_passengers

    def __str__(self):
        return super().__str__() + f'Всего денег заработал: {self.money}\nВсего пассажиров перевез: ' \
                                   f'{Bus.count_passengers}\nСейчас пассажиров: {self.passengers}'