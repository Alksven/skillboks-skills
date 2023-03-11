from house import House
from residents import Husband
from residents import Wife
from residents import Cat

house = House()
husband = Husband(name='Владимир', house=house)
wife = Wife(name='Валентина', house=house)
cat = Cat(name='Барсик', house=house)

list_house_residents = [husband, wife, cat]