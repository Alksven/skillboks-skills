import random

class Toyota:
    color = 'red'
    price = 1000000
    max_speed = 200
    speed_now = 0

    def info(self):
        print(self.color)
        print(self.price)
        print(self.max_speed)
        print(self.speed_now)

    def spped(self, speed):
        print('Текущая скорость: ', speed)

info_car = Toyota()
info_car.info()

speed_car = Toyota()
speed_car.spped(100)