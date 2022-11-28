import random

first_list = [random.randint(1, 100) for _ in range(10)]
ready_list = []
print('Изначальный Список', first_list)
print('\nВариант 1')


for i in range(0, len(first_list), 2):
    number = (first_list[i], first_list[i + 1])
    ready_list.append(number)
print(ready_list)


print('Вариант 2')

ready_list_2 = [(n, first_list[i + 1]) for i, n in enumerate(first_list) if i % 2 == 0]
print(ready_list_2)






