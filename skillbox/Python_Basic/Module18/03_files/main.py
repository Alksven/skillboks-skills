name_file = input('Название файла: ')
sym_list = list('@№$%^&*()')

for sym in sym_list:
    if name_file.startswith(sym):
        print('Ошибка: название начинается на один из специальных символов.')
        exit()

if not name_file.endswith(('.txt', '.docx')):
    print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx.')

else:
    print('Файл назван верно.')
