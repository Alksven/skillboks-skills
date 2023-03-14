class House:
    def __init__(self):
        self.money = 100
        self.food_people = 50
        self.food_cat = 30
        self.dirt = 0

    def __str__(self):
        return f'\nДенег: {self.money}\nЕды для людей: {self.food_people}\nЕды для кота: {self.food_cat}\nЧистота: {self.dirt}'