num_of_num = int(input('Введите число: '))

answer_list = ['1' if i % 2 == 0 else i % 5 for i in range(num_of_num)]

print('Результат:', answer_list)
