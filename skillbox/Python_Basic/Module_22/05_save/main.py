import os

def create_file(path_file):
        txt_open = open(path_file, 'w')
        txt_open.write(new_text)
        txt_open.close()


def change_file(path_file):
        choice_new_file = input('Хотите создать новый файл или выйти из программы? (новый\выйти): ').lower()
        if choice_new_file == 'новый':
            new_name = input('Введите имя нового файла: ')+'.txt'
            path_file.remove(path_file[-1])
            path_file.append(new_name)
            new_ready_path = os.sep.join(path)
            create_file(new_ready_path)
            print('Файл успешно сохранён!')
        else:
            print('Работа программы завершена')
            exit()




new_text = input('Введите строку: ')
print('Куда хотите сохранить документ? '
      'Введите последовательность папок (через пробел): ')
path = input().split()

name_file = input('Введите имя файла:')+'.txt'

path.append(name_file)
ready_path = os.sep.join(path)
flag = os.path.isfile(ready_path)

if flag == False:
    create_file(ready_path)
    print('Файл успешно сохранён!')
else:
    choice = input('Вы действительно хотите перезаписать файл? (да.нет) ').lower()
    if choice == 'да':
        create_file(ready_path)
        print('Файл успешно перезаписан!')
    else:
        change_file(path)
