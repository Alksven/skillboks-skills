import os


def gen_files_path(directory):
    for current_directory, subdirectories, files in os.walk(directory):
        yield current_directory


root_directory = os.path.abspath(os.sep)
files_path = gen_files_path(root_directory)

search = input('Какйо каталог ищем? ')
for path in files_path:
    if path.endswith(search):
        print('Каталог найден.\nСписок файлов:')
        path_2 = os.path.abspath(path)
        for i_2 in os.listdir(path_2):
            print(os.path.join(path_2, i_2))
