people_num = int(input('Введите количество человек: '))
people_dict = dict()
count_pep = 0
for count in range(people_num):
    person_parents = input(f'{count} пара: ').split()
    people_dict[count] = person_parents
for i_2 in people_dict.values():
    person_num = function()


print(people_dict)

# Введите количество человек: 9
#
# Первая пара: Alexei Peter_I
#
# Вторая пара: Anna Peter_I
#
# Третья пара: Elizabeth Peter_I
#
# Четвёртая пара: Peter_II Alexei
#
# Пятая пара: Peter_III Anna
#
# Шестая пара: Paul_I Peter_III
#
# Седьмая пара: Alexander_I Paul_I
#
# Восьмая пара: Nicholaus_I Paul_I