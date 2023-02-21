from classes import Person
from classes import House
import random


house = House()
person_1 = Person('Вася', house)
person_2 = Person('Петя', house)
num_day = 1
while num_day != 366:
    print('{} день'.format(num_day))
    for person in Person.list_person:
        cube = random.randint(1, 6)
        if person.satiety <= 0:
            print('{} помер на {} день.'.format(person.name, num_day - 1))
            Person.list_person.remove(person)
        else:
            if person.satiety < 20:
                person.eat(random.randint(5, 10))
                print('{} поел. Сытость {}. Осталось еды {}'.format(
                    person.name, person.satiety, house.food))

            elif house.food < 10:
                person.go_shopping(random.randint(10, 15))
                print('{} сходил в магазин. Денег осталось {}. Еды в доме теперь {}'.format(
                    person.name, house.money, house.food))

            elif house.money < 50:
                person.work(random.randint(15, 20))
                print('{} пошел работать. Потратил калории, сытость {}. Но заработал. Денег {}'.format(
                    person.name, person.satiety, house.money))

            elif cube == 1:
                person.work(random.randint(15, 20))
                print('{} пошел работать. Потратил калории, сытость {}. Но заработал. Денег {}'.format(
                    person.name, person.satiety, house.money))

            elif cube == 2:
                person.eat(random.randint(5, 10))
                print('{} поел. Сытость {}. Осталось еды {}'.format(
                    person.name, person.satiety, house.food))

            else:
                person.play(random.randint(5, 10))
                print('{} поиграл. Проголодался. Сытость {}'.format(person.name, person.satiety))
        if len(Person.list_person) == 0:
            print('Ни кто не выжил.')
            exit()
    num_day += 1
