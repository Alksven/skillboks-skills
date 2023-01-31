import os

def search(path):
    for i in os.listdir(path):
        if os.path.isfile(os.path.join(path, i)):
            count_file.append('1')
            count_kb.append(os.path.getsize(os.path.join(path, i)))
        elif os.path.isdir(os.path.join(path, i)):
            count_fol.append('1')
            search(os.path.join(path, i))



path = input('Введите путь: ')

count_kb = []
count_fol = []
count_file = []

search(os.path.abspath(path))

print('Размер каталога (в Кб):', sum(count_kb) / 1024)
print('Количество подкаталогов: ', len(count_fol))
print('Количество файлов: ', len(count_file))


