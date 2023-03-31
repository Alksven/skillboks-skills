
class Robot:
    def __init__(self, model: str) -> None:
        self.model = model

    def operate(self):
        print('Я — Робот')

    def __str__(self):
        return f'Модель: {self.model}'


class CanFly:

    def __init__(self):
        self.altitude = 0
        self.speed = 0
        self.distance = 0

    def take_off(self):
        self.distance_on()
        if self.altitude == 3:
            print('Достигнута максимальная высота.')
        else:
            self.altitude += 1
            print(f'Высота {self.altitude}')

    def fly(self):
        self.distance_on()
        if self.speed == 3:
            print('Достигнута максимальная скорость.')
        else:
            self.speed += 1
            print(f'Текущая скорость {self.speed}')

    def land(self):
        self.distance_on()
        if self.altitude == 0:
            print('Приземление прошло успешно')
            self.speed = 0
        else:
            self.altitude -= 1
            print(f'Высота {self.altitude}')

    def distance_on(self):
        self.distance += self.speed
        print(f'Пройденная дистанция: {self.distance}')

    def __str__(self):
        return f'Высота: {self.altitude} Скорость: {self.speed} Растояние: {self.distance}'


class ReconnaissanceDrone(Robot, CanFly):

    def __init__(self, model: str):
        Robot.__init__(self, model)
        CanFly.__init__(self)


    def operate(self):
        print('Веду разведку с воздуха')
        self.speed += 1

    def __str__(self):
        return f'{Robot.__str__(self)}\n{CanFly.__str__(self)}'


class MilitaryDrone(Robot, CanFly):

    def __init__(self, model: str, gun: str):
        Robot.__init__(self, model)
        CanFly.__init__(self)
        self.gun = gun

    def operate(self):
        print(f'Ведется защита военного объекта с помощью {self.gun}')
        self.speed += 1

    def __str__(self):
        return f'{Robot.__str__(self)}\nОружие: {self.gun}\n{CanFly.__str__(self)}'


dron_cear = MilitaryDrone(model='t1000', gun='Воздушка')
dron_cear.take_off()
dron_cear.take_off()
dron_cear.fly()
dron_cear.fly()
dron_cear.operate()
print(dron_cear)

