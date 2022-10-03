win_people = 0
num_of_skates = int(input('Кол-во коньков: '))
skates_list = []

for count_skate in range(num_of_skates):
    print(f'Размер {count_skate + 1}-й пары:', end=' ')
    skate_size = int(input())
    skates_list.append(skate_size)

skates_list = sorted(skates_list)

num_of_people = int(input('Кол-во Людей: '))
people_list = []

for count_people in range(num_of_people):
    print(f'Размер ноги {count_people + 1}-го человека:', end=' ')
    people_size = int(input())
    people_list.append(people_size)

people_list = sorted(people_list)

for elem_people in people_list:
    if skates_list.count(elem_people) >= 1:
        skates_list.remove(elem_people)
        win_people += 1
    else:
        for elem_skate in skates_list:
            if people_list.count(elem_skate) >= 1:
                continue
            if elem_skate > elem_people:
                skates_list.remove(elem_skate)
                win_people += 1
                break
print('Наибольшее кол-во людей, которые могут взять ролики:', win_people)
