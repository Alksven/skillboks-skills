first_list = list(input('Первая строка: '))
second_list = list(input('Вторая строка: '))
count = 0

for i in range(len(second_list)):
    if first_list == second_list:
        print('Первая строка получается из второй со сдвигом', count)
        break
    else:
        second_list.append(second_list[0])
        second_list.remove(second_list[0])
        count += 1
else:
    print('Первую строку нельзя получить из второй с помощью циклического сдвига.')