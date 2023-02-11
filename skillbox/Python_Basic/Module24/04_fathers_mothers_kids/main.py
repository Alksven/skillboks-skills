from classes import Parent
from classes import Child
import random

def age_check(parent, count):
    name, age = input("Введите имя и возраст {}го ребенка: ".format(count)).split()
    while int(parent) - int(age) < 16:
        age = int(input("Возраст слишком большой, пожалуйста, введите правильный возраст: "))
    return name, age


number_of_parents = int(input('Количество родителей? '))
for _ in range(number_of_parents):
    name_parent, age_parent = input("\nВведите имя и возраст родителя: ").split()
    Parent(name_parent, age_parent)
    have_many_children = int(input('Сколько детей у этого родителя? '))

    if have_many_children > 0:
        for count_children in range(have_many_children):
            name_child, age_child = age_check(Parent.parents_list[-1].age, count_children + 1)
            Child(name_child, age_child)
            Parent.parents_list[-1].children_list.append(Child.children[-1])
            Child.children[-1].parent.append(Parent.parents_list[-1])



while True:
    print()
    for i, person in enumerate(Parent.parents_list):
        print(i + 1, '=', person.name)
    choose_parent = int(input('Выберите родителя: '))
    choice = int(input('1 = Показать информацию о родителе.\n2 = Перейти к воспитанию детей.\n3 = Вернуться к списку родителей.\n'))
    if choice == 3:
        continue
    elif choice == 1:
        Parent.parents_list[choose_parent - 1].tell_about_yourself()
    elif choice == 2:
        if len(Parent.parents_list[choose_parent - 1].children_list) > 0:
            choose_child = random.randint(1, len(Parent.parents_list[choose_parent - 1].children_list))
            choice_of_behavior = random.randint(1, 2)
            if choice_of_behavior == 1:
                Parent.parents_list[choose_parent - 1].children_list[choose_child - 1].state_calm()
            else:
                Parent.parents_list[choose_parent - 1].children_list[choose_child - 1].state_hungry()
        else:
            print('Нет детей')
    else:
        print('Вы ввели не правильную команду')