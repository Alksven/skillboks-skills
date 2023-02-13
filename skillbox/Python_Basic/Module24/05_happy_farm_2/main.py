from classes import Potato
from classes import Garden
plant_potatoes = input('Plant potatoes? ').lower()
if plant_potatoes == 'yes':
    for i in range(5):
        Potato(f'Potato_{i + 1}')

for i in Garden.potato_list:
    i.info_about_Potato()
