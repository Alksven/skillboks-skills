message = input('Введите шаблон поздравления, в шаблоне можно использовать конструкцию {name} и {age}:')
name = input('Список людей через запятую: ').split(', ')
age = input('Возраст людей через пробел: ')
ages = [int(i_number) for i_number in age.split()]

for i_man in range(len(name)):
    print(message.format(
        name=name[i_man],
        age=ages[i_man]))

people = [' '.join([name[i_man], str(ages[i_man])]) for i_man in range(len(name))]
people_str = ', '.join(people)

print('\nИменинники', people_str)