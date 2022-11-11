num_of_order = int(input('Введите количество заказов: '))
order_dict = dict()

for num_order in range(num_of_order):
    name, pizza, amount = input(f'{num_order + 1} заказ ').split()
    amount = int(amount)
    if name not in order_dict:
        order_dict[name] = {pizza: amount}
    else:
        if pizza not in order_dict[name]:
            order_dict[name] |= {pizza: amount}
        else:
            order_dict[name][pizza] += amount

for name, order in sorted(order_dict.items()):
    print(f'{name}:')
    for pizza, amount in sorted(order.items()):
        print('    ', pizza, amount)