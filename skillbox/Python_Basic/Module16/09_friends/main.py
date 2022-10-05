num_of_friends = int(input('Кол-во друзей: '))
num_of_debt = int(input('Долговых расписок: '))
friends_list = []

for add_people in range(1, num_of_friends + 1):
    friends_list.append([add_people, 0])


for count in range(num_of_debt):
    print(f'{count + 1}-я расписка')
    to_whom = int(input('Кому: '))
    from_whom = int(input('От кого: '))
    how_many = int(input('Сколько: '))
    friends_list[to_whom - 1][1] += how_many * -1
    friends_list[from_whom - 1][1] += how_many
    print()

print('Баланс друзей:')
for balance in range(len(friends_list)):
    print(f'{balance + 1}: {friends_list[balance][1]}')
