num_of_people = int(input('Кол-во человек:'))
people_list = list(range(1, num_of_people + 1))


delete_number = int(input('Какое число в считалке? '))
print(f'Значит, выбывает каждый {delete_number}-й человек')
delete_people = people_list[0]

while len(people_list) > 0:
    print('Текущий круг людей:', people_list, '\nНачало счёта с номера', delete_people)
    delete_people = people_list[delete_number % len(people_list)]
    print(f'Выбывает человек под номером {people_list[delete_people - 1]}')
    people_list.remove(people_list[delete_people - 1])
