import os

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

ready_txt_file = open('scripts.txt', 'a')

for path_file in ready_list:
    time_file = open(path_file, 'r')
    for i_2 in time_file:
        ready_txt_file.write(i_2)
    time_file.close()
    ready_txt_file.write('\n'+('*' * 40)+'\n')
    ready_txt_file.write('\n')

ready_txt_file.close()



