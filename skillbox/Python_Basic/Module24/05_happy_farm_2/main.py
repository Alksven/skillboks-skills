from classes import Gardener
from classes import Garden
import random

name_gar = input('Как звать садовника? ')
count_potato = int(input('Сколько картошки посадим?'))
my_garden = Garden(count_potato)
gardener = Gardener(name_gar, my_garden)

for i in range(3):
    my_garden.grow_all()
    if my_garden.are_all_ripe():
        gardener.harvest()
        break
    else:
        care = random.randint(0, 1)
        if care == 1:
            gardener.care()
            if my_garden.are_all_ripe():
                gardener.harvest()
                break
