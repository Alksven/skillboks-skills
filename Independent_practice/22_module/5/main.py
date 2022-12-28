import os

def find_file(cup_path, file):
    for i_elem in os.listdir(cup_path):
        path = os.path.join(cup_path, i_elem)
        if file == i_elem:
            print(path)
        if os.path.isdir(path):
            result = find_file(path, file)
            if result:
                print(path)



path_to = input('enter the path: ')
name_file = input('enter file name: ')

print('Found the following paths:')
find_file(path_to, name_file)



