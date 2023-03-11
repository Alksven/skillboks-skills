from house import House
import random


class HouseResidents:

    def __init__(self, name, house):
        self.name = name
        self.house = house
        self.satiety = 30


    def eat(self):
        self.satiety += random.randint(10, 30)

    def satiety_consumption(self):
        self.satiety -= 10
        if self.satiety <= 0:
            print({self.name}, 'умер')
            return self.__class__.__name__



class Person():

    def __init__(self):
        self.happiness = 100

    def touch_cat(self):
        self.happiness += 5
        HouseResidents.satiety_consumption(self)



class Pet:

class Husband(HouseResidents, Person):
    def __init__(self, name, house):
        super().__init__(name, house)

    def play(self):
        self.satiety_consumption()


    def work(self):
        self.satiety_consumption()


class Wife(HouseResidents, Person):
    def __init__(self, name, house):
        super().__init__(name, house)

    def buy_products(self):
        self.satiety_consumption()

    def buy_coat(self):
        self.satiety_consumption()

    def housework(self):
        self.satiety_consumption()


class Cat(HouseResidents, Pet):

    def __init__(self, name, house):
        super().__init__(name, house)

    def eat(self):
        self.satiety += random.randint(5, 10) * 2

    def sleep(self):
        self.satiety_consumption()

    def tear_wallpaper(self):
        self.satiety_consumption()




