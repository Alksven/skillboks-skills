from classes import *
import random

# Вода 1 + Воздух 12 = Шторм 13
# Вода 1 + Огонь 21 = Пар 22
# Вода 1 + Земля 31 = Грязь 32
# Воздух 12 + Огонь 21 = Молния 33
# Воздух 12 + Земля 31 = Пыль 43
# Огонь 21 + Земля 31 = Лава 52
def check(first, second):
    num_new_element = first.num + second.num
    new_elements = {
        13: 'Шторм',
        22: 'Пар',
        32: "Грязь",
        33: 'Молния',
        43: 'Пыль',
        52: 'Лава'
    }
    if first.num == second.num:
        print('Синтез между одним элементом невозможен.')
        return None
    else:
        print('Вы синтезируете  {} и {}. Создан новый элемент {}.'.format(
            first.element,
            second.element,
            new_elements[num_new_element]))
        return True


elements = [Air(12), Water(1), Fire(21), Earth(31)]

action = 1
while action != 0:
    action = int(input('1 = Новый синтез.\n0 = Выход\nВвод: '))
    if action == 0:
        print('Программа завершена.')
    if action == 1:
        first_element = random.randint(0, len(elements) - 1)
        second_element = random.randint(0, len(elements) - 1)
        if check(elements[first_element], elements[second_element]):
            new_element = elements[first_element] + elements[second_element]
            print(new_element)
