def function(name, n_o_n):
    list_number = []
    for count in range(n_o_n):
        print(f'Введите {count + 1}-е число для {name} списка:', end=' ')
        number = int(input())
        list_number.append(number)
    return list_number


list_1 = function('первого', 3)
list_2 = function('второго', 7)

print('Первый список:', list_1, '\nВторой список:', list_2)

list_1.extend(list_2)

for i in list_1:
    while list_1.count(i) != 1:
        list_1.remove(i)

print('Новый первый список с уникальными элементами:', list_1)
