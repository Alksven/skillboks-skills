import math

class Car:

    def __init__(self, x, y, a):
        self.x = x
        self.y = y
        self.a = math.radians(a)

    def forward_movement(self):
        distance = float(input('На какое расстояние проехала машина?'))
        self.x = self.x + distance * math.cos(self.a)
        self.y = self.y + distance * math.sin(self.a)
        print('new X:', round(self.x, 1))
        print('new Y', round(self.y, 1))




    def turn(self):
        pass



class Bus(Car):
    pass