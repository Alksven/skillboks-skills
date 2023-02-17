from classes import Gardener
from classes import Garden
import random

name_gar = input('Как звать садовника? ')
count_potato = int(input('Сколько картошки посадим?'))
my_garden = Garden(count_potato)
gardener = Gardener(name_gar, my_garden)

while True:
    my_garden.grow_all()
    a = int(input('Что делаем? 1 продолжить 2 собрать урожай'))
    if a == 1:
        gardener.drink_gardener()










