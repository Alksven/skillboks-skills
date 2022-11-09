num_of_order = 2 #int(input('Введите количество заказов: '))
order_dict = dict()
client = ''
pizza = ''
count = 0
for num_order in range(num_of_order):
    add_order = input(f'{num_order + 1} заказ ').split()
    client = add_order[0]
    pizza = add_order[1]
    if client == order_dict[0]['client'] and pizza == order_dict[0]['pizza']:
        order_dict[0]['amount'] += int(add_order[2])
    else:
        count += 1
        order_dict[count] = {'client': add_order[0], 'pizza': add_order[1], 'amount': int(add_order[2])}

print(order_dict)

# Иванов Пепперони 1
# Петров Де-Люкс 2
# Иванов Мясная 3