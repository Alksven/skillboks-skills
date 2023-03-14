from house import House
from residents import HouseResidents
from residents import Husband
from residents import Wife
from residents import Cat


house = House()
husband = Husband(name='Владимир', house=house)
wife = Wife(name='Валентина', house=house)
cat = Cat(name='Мурзик', house=house)

list_house_residents = [husband, wife, cat]


for day in range(1, 366):
    print(f'День {day}')
    house.dirt += 5
    print(house)

    for person in list_house_residents[:]:
        if isinstance(person, Husband):
            person.action_husband()
        elif isinstance(person, Wife):
            person.action_wife()
        elif isinstance(person, Cat):
            person.action_cat()

        if person.satiety < 1:
            list_house_residents.remove(person)

    if len(list_house_residents) == 0:
        print('Все умерли')
        break

    day += 1
    if house.dirt > 90:
        husband.heppy_down()
        wife.heppy_down()

print("\nИтоги года:")
print(f'{husband.name} заработал за год: {Husband.money_full}')
print(f'{wife.name} купила шуб за год: {Wife.coat_full}')
print(f'{wife.name} и {husband.name} съели за год: {HouseResidents.count_people_food}')
print(f'{cat.name} съели за год: {HouseResidents.count_cat_food}')





