from classes import Gardener
from classes import Garden
import random

gardener = Gardener('Василий')
my_garden = Garden()
while True:
    my_garden.grow_all()
    gardener_state = random.randint(0, 1)
    if gardener_state == 0:




