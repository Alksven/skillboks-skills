def function(name, people_dict):
    name_count = dict()
    for i_name in people_dict.values():
        if name == i_name[0]:










people_num = int(input('Введите количество человек: '))
all_people = set()
people_dict = dict()

for count in range(people_num):
    person_parents = input(f'{count} пара: ').split()
    all_people.add(person_parents[0])
    all_people.add(person_parents[1])
    people_dict[count] = person_parents

for name in all_people:
    function(name, people_dict)


print(people_dict)
print(all_people)

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