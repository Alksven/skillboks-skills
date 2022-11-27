import random

first_list = [random.randint(1, 100) for _ in range(10)]
ready_list = []
print('Вариант 1')
for i in range(0, len(first_list), 2):
    number = (first_list[i], first_list[i + 1])
    ready_list.append(number)
print(ready_list)
print(first_list)

print('Вариант 3')
list_1 = [n for i, n in enumerate(first_list) if i % 2 == 0]
list_2 = [n for i, n in enumerate(first_list) if i % 2 != 0]
ready_list_2 = [(zip(list_1, list_2))]
print(ready_list_2)
print(list_1)
print(list_2)

