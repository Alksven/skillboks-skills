from classes import Potato
from classes import Garden
import random

def plant_potatoes():
    for i in range(5):
        Potato(f'Potato_{i + 1}')

actions_list = ['\n1 = Plant potatoes', '2 = Garden information', 'Harvest', 'Water potatoes']
while True:
    for i in actions_list:
        print(i)

    actions = int(input('\nWhat are we doing? '))
    if actions == 1 and len(Garden.potato_list) == 0:
        if len(Garden.potato_list) == 0:
            plant_potatoes()
        else:
            print('The potatoes have already been planted.')

    elif actions == 2:
        if len(Garden.potato_list) > 0:
            print('Grow in the garden:')
            for i in Garden.potato_list:
                Garden.garden_information(i)
            info_pot = int(input('Get information about the status of each potato?\n(1 = Yes/ 2 = No '))
            if info_pot == 1:






