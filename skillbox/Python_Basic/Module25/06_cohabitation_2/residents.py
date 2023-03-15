from house import House
import random


class HouseResidents:

    count_people_food = 0
    count_cat_food = 0

    def __init__(self, name, house):
        self.name = name
        self.house = house
        self.satiety = 30

    def eat(self):
        print(f'\n<<< {self.name} поел(a) >>>')
        food = random.randint(10, 30)
        HouseResidents.count_people_food += food
        self.satiety += food
        self.house.food_people -= food
        if self.house.food_people < 0:
            self.house.food_people = 0
        print(self)

    def satiety_down(self):
        self.satiety -= 10
        if self.satiety <= 0:
            self.satiety = 0
            print(f'XXXXXXXXX {self.name} умер XXXXXXXXXX')
        else:
            print(self)

    def __str__(self):
        return f'\nПоказатели {self.name}:\nСытость: {self.satiety}'


class Human:

    def __init__(self):
        self.happiness = 100

    def touch_cat(self):
        print(f'\n<<< {self.name} погладил кота >>>')
        self.happiness += 5
        self.satiety_down()

    def heppy_down(self):
        if self.satiety > 0:
            print(f'\n{self.name} стал на 10 пунктов несчастным')
            self.happiness -= 10
            if self.happiness < 10:
                print(f'{self.name} умер(ла) от депрессии.')

    def __str__(self):
        return f'\nСчастье: {self.happiness}'


class Pet:
    pass


class Husband(HouseResidents, Human):

    money_full = 0

    def __init__(self, name, house):
        HouseResidents.__init__(self, name, house)
        Human.__init__(self)

    def play(self):
        print(f'\n<<< {self.name} поиграл >>>')
        self.happiness += 20
        self.satiety_down()

    def work(self):
        print(f'\n<<< {self.name} заработал 150 рублей >>>')
        self.house.money += 150
        Husband.money_full += 150
        self.satiety_down()

    def __str__(self):
        return HouseResidents.__str__(self) + Human.__str__(self)

    def action_husband(self):
        if self.house.money < 100:
            self.work()
        elif self.satiety < 15 and self.house.food_people > 0:
            self.eat()
        elif self.happiness < 20:
            self.play()
        else:
            self.touch_cat()


class Wife(HouseResidents, Human):

    coat_full = 0

    def __init__(self, name, house):
        HouseResidents.__init__(self, name, house)
        Human.__init__(self)

    def buy_products(self):
        print(f'\n<<< {self.name} купила всем еды в тои числе и коту >>>')
        self.house.money -= 20
        if self.house.money < 0:
            self.house.money = 0
        self.house.food_people += 10
        self.house.food_cat += 10
        self.satiety_down()

    def buy_coat(self):
        print(f'\n<<<{self.name} купила шубу >>>')
        self.house.money -= 350
        self.happiness += 60
        Wife.coat_full += 1
        self.satiety_down()

    def housework(self):
        if self.house.dirt < 1:
            print('В доме чисто')
            return None
        else:
            print(f'\n<<<{self.name} убралась в доме >>>')
            count_dirt = random.randint(1, self.house.dirt)
            self.house.dirt -= count_dirt
            print(f'{self.name} убрала {count_dirt} грязи')
            self.satiety_down()

    def __str__(self):
        return HouseResidents.__str__(self) + Human.__str__(self)

    def action_wife(self):
        if self.house.food_people < 20 and self.house.money > 10:
            self.buy_products()
        elif self.satiety < 15 and self.house.food_people > 0:
            self.eat()
        elif self.happiness < 20:
            self.buy_coat()
        elif self.house.dirt > 10:
            self.housework()
        else:
            self.touch_cat()


class Cat(HouseResidents, Pet):

    def __init__(self, name, house):
        super().__init__(name, house)

    def eat(self):
        print(f'\n<<< {self.name} поел(a) >>>')
        food = random.randint(5, 10)
        HouseResidents.count_cat_food += food
        self.satiety += food * 2
        self.house.food_cat -= food
        if self.house.food_cat < 0:
            self.house.food_cat = 0
        print(self)

    def sleep(self):
        print(f'\n<<< {self.name} поспал(a) >>>')
        self.satiety_down()

    def tear_wallpaper(self):
        print(f'\n<<< {self.name} подрал обои >>>')
        self.house.dirt += 5
        self.satiety_down()

    def __str__(self):
        return HouseResidents.__str__(self)

    def action_cat(self):
        if self.satiety <= 10 and self.house.food_cat > 0:
            self.eat()
        else:
            action = random.randint(1, 2)
            if action == 1:
                self.sleep()
            if action == 2:
                self.tear_wallpaper()