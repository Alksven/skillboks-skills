num_of_num = int(input('Кол-во чисел: '))
number_list = []
help_list = []
flag = True

for count in range(num_of_num):
    number = int(input('Число: '))
    if number_list.count(number) > 0:
        flag = False
    number_list.append(number)

print('Последовательность:', number_list)

if flag:
    number_list = list(reversed(number_list))
    number_list.remove(number_list[0])
    print(f'Нужно приписать чисел: {len(number_list)} \nСами числа: {number_list}')

else:
    for count in range(len(number_list), -1, -1):
        if number_list[count] == number_list[count - 1]:
