contacts = dict()
selection = 0

while selection != 3:
    selection = int(input('\nВведите номер действия:\n1. Добавить контакт.\n2. Найти человека.\n3. Выход.\n'))
    if selection == 1:
        add_contact = input('Введите имя и фамилию нового контакта (через пробел): ').title().split()

        for i_person in contacts:
            if add_contact[0] in i_person and add_contact[1] in i_person:
                print('Такой человек уже есть в контактах.')
                break
        else:
            add_number = int(input('Введите номер телефона:'))
            contacts[add_contact[0], add_contact[1]] = add_number

    if selection == 2:
        contact_search = input('Введите фамилию для поиска: ').title()
        for search in contacts:
            if contact_search in search:
                print(*search, contacts[search])

    print('\nТекущий словарь контактов:', contacts)
    print('=' * 60)