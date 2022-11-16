text = input('Введите строку: ')
text_dict = dict()

for symbol in text:
    if symbol not in text_dict.keys():
        text_dict[symbol] = 1
    else:
        text_dict[symbol] += 1
count = 0
for amount in text_dict.values():
    if amount % 2 != 0:
        count += 1
        if count == 2:
            print('Нельзя сделать палиндромом')
            break

if count == 1 or count == 0:
    print('Можно сделать палиндромом')