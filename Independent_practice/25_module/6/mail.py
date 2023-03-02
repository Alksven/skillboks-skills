from classes import *
import random

soldier = Soldier()
civilian_man = CivilianMan()

while True:
    damage = random.randint(0, 15)
    action = int(input(f'\nDeal {damage} damage? '))
    if action == 1:
        soldier.damage(damage)
        print(soldier)
        civilian_man.damage(damage)
        print(civilian_man)
        if soldier.health <= 0 or civilian_man.health <= 0:
            print('GAME OVER')
            break
