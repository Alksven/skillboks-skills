from datetime import datetime

def see_chat():
    with open('chat.txt', 'r') as chat:
        for i in chat:
            print(i[0:len(i) - 1])

def message_chat():
    name = input('Введите ваше имя ')
    message = input('Введите сообщение: ')
    with open('chat.txt', 'a') as chat:
        time = datetime.today()
        chat.write(str(time) + '--- ' + '[ ' + name + ' ]  ' + message + '\n')


while True:
    select_action = input('Посмотреть чат (Нажмите "Ч")\nНаписать сообщение (Нажмите "С")\n').lower()
    if select_action == 'ч' or select_action == 'x':
        see_chat()
    elif select_action == 'с' or select_action == 'c':
        message_chat()
