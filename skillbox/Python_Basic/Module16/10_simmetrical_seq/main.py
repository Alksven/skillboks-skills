num_of_num = int(input("Кол-во чисел: "))

if num_of_num == 1:
    print('Недостаточно чисел для вычисления.')
    exit()
number_list = []
reverse_number_list = []

for _ in range(num_of_num):
    number = int(input("Число: "))
    number_list.append(number)

print("\nПоследовательность: ", number_list)

for index in range(len(number_list) - 1, -1, -1):
    reverse_number_list.append(number_list[index])

while True:

    if number_list == reverse_number_list:
        print('Последовательность являются симметричной', number_list)
        exit()
    elif number_list[len(number_list) - 1] == reverse_number_list[0]:
        reverse_number_list.remove(reverse_number_list[0])
    else:
        break

print(f'Нужно приписать чисел: {len(reverse_number_list)} \nСами числа: {reverse_number_list}')
