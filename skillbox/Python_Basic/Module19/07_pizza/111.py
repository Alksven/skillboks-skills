num_of_order = 2 #int(input('Введите количество заказов: '))
order_dict = dict()
client = []

count = 1
for num_order in range(num_of_order):
    add_order = input(f'{num_order + 1} заказ ').split()
    if num_order == 0:
        order_dict[add_order[0]] = {'pizza': add_order[1], 'amount': int(add_order[2])}
        continue
    if add_order[0] in order_dict and order_dict[add_order[0]]['pizza'] != add_order[1]:
        order_dict[add_order[0]] = {'pizza': add_order[1], 'amount': int(add_order[2])}
    if add_order[0] in order_dict and order_dict[add_order[0]]['pizza'] == add_order[1]:
        order_dict[add_order[0]]['amount'] += int(add_order[2])
    else:
        order_dict[add_order[0]] = {'pizza': add_order[1], 'amount': int(add_order[2])}



print(order_dict)

# Иванов Пепперони 1
# Петров Де-Люкс 2
# Иванов Мясная 3