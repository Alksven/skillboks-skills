message = input('Сообщение: ') + ' '
new_message = ''
help_list = []

for i in message:
    if i.isdigit() or i.isalpha():
        help_list.append(i)
    else:
        help_list.reverse()
        new_message += ''.join(help_list)
        new_message += i
        help_list = []

print('Новое сообщение:', new_message)


