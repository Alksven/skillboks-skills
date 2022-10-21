message = input('Сообщение: ')
new_message = ''
help_list = []

for i in range(len(message)):
    if message[i].isdigit() or message[i].isalpha():
        help_list.append(message[i])
    else:
        help_list.reverse()
        new_message += ''.join(help_list)
        new_message += (message[i])
        help_list = []

print('Новое сообщение:', new_message)


