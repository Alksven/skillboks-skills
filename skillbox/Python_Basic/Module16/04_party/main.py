guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

command = ''
while command != 'Пора спать':
    print(f'Сейчас на вечеринке {len(guests)} человек: {guests}')
    command = input('Гость пришел или ушел? ')

    if command == 'пришел':
        guest_name = input('Имя гостя: ')
        print('Привет ', guest_name)

        if len(guests) > 5:
            print(f'Прости, {guest_name}, но мест нет.')
            print()
            continue
        guests.append(guest_name)

    if command == 'ушел':
        guest_name = input('Имя гостя: ')
        guests.remove(guest_name)
        print('Пока,', guest_name)

    print()

print('Вечеринка закончилась, все легли спать.')
