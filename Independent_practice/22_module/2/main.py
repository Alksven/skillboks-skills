import os

def print_dirs(folder):
    print('\nDirectory contents:', folder)
    for i_elem in os.listdir(folder):
        path = os.path.join(folder, i_elem)
        print('    ', path)


folder_list = ['Загрузки']

for i_folder in folder_list:
    path_to_folder = os.path.abspath(os.path.join('..', '..', '..', '..', '..', i_folder))
    print_dirs(path_to_folder)

