import os
import random

def find_file(cup_path, file):
    for i_elem in os.listdir(cup_path):
        path = os.path.join(cup_path, i_elem)
        if file == i_elem:
            ready_list.append(path)
        if os.path.isdir(path):
            find_file(path, file)


path_to = '/home/ven/my_projects/skillboks-skills/Independent_practice'
name_file = 'main.py'
ready_list = []

find_file(path_to, name_file)

sel_file = random.randint(0, len(ready_list))
file = open(ready_list[sel_file], 'r')

for i in file:
    print(i)
file.close()
