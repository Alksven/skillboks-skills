from house import House
import random


class HouseResidents:

    def __init__(self, name, house):
        self.name = name
        self.house = house
        self.satiety = 30


    def eat(self):
        print('поел')
        self.satiety += random.randint(10, 30)

    def satiety_down(self):
        self.satiety -= 10
        if self.satiety <= 0:
            print({self.name}, 'умер')
            return self.__class__.__name__



class Human:

    def __init__(self):
        self.happiness = 100

    def touch_cat(self):
        self.happiness += 5
        self.satiety_down()

    def heppy_down(self):
        print(f'{self.}')
        self.happiness -= 10





class Pet:
    pass

class Husband(HouseResidents, Human):
    def __init__(self, name, house):
        HouseResidents.__init__(self, name, house)
        Human.__init__(self)

    def play(self):
        self.satiety_down()


    def work(self):
        print('зараборал 150')
        self.house.money += 150
        self.satiety_down()


class Wife(HouseResidents, Human):
    def __init__(self, name, house):
        super().__init__(name, house)

    def buy_products(self):
        self.house.money -= 20
        self.house.food_people += 10
        self.house.food_cat += 10
        self.satiety_down()

    def buy_coat(self):
        self.house.money -= 350
        self.satiety_down()

    def housework(self):
        count_dirt = random.randint(1, self.house.dirt)
        self.house.dirt -= count_dirt
        print(f'{self.name} убрала {count_dirt} грязи')
        self.satiety_down()


class Cat(HouseResidents, Pet):

    def __init__(self, name, house):
        super().__init__(name, house)

    def eat(self):
        self.satiety += random.randint(5, 10) * 2

    def sleep(self):
        self.satiety_down()

    def tear_wallpaper(self):
        print(f'{self.name} дерет обои')
        self.house.dirt += 5
        self.satiety_down()




