def ask_users(qw,
              comp='Неверный ввод. Пожалуйста, введите "да" или "нет"',
              ret=4):
    while True:
        answer = input(qw).lower()
        if answer == 'да':
            return 1
        elif answer == 'нет':
            return 0
        ret -= 1
        if ret == 0:
            print('Количество попыток истекло.')
            break
        print(comp)
        print("Осталось попыток", ret)



ask_users('Вы действительно хотите выйти?')
ask_users('Удалить файл?', 'Так удалить или нет?')
ask_users('Записать файл?', ret=2)