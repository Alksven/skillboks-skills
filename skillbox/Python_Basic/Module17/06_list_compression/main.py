import random

num_of_num = int(input('Количество чисел в списке: '))

num_list = [random.randint(0, 2) for _ in range(num_of_num)]
answer_list = [i for i in num_list if i != 0]

print('Список до сжатия: ', num_list, '\nСписок после сжатия:', answer_list)
