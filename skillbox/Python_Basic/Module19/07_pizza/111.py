num_of_order = 2 #int(input('Введите количество заказов: '))
order_dict = dict()

count = 0
for num_order in range(num_of_order):
    add_order = 'Иванов Мясная 3'.split()

    for count in order_dict.values():
        if count['client'] == add_order[0] and count['pizza'] == add_order[1]:
            order_dict[0]['amount'] += int(add_order[2])
        else:
            count += 1
            order_dict[count] = {'client': add_order[0], 'pizza': add_order[1], 'amount': int(add_order[2])}

print(order_dict)

