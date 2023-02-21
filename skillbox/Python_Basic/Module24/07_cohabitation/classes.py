class Person:
    list_person = []

    def __init__(self, name, house):
        self.name = name
        self.satiety = 50
        self.house = house
        self.list_person.append(self)

    def eat(self, num):
        self.satiety += num
        self.house.food -= num

    def work(self, num):
        self.satiety -= num
        self.house.money += num

    def play(self, num):
        self.satiety -= num

    def go_shopping(self, num):
        self.house.food += num
        self.house.money -= num


class House:

    def __init__(self):
        self.food = 50
        self.money = 0

