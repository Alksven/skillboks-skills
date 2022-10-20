def number_count(password, numbers):
    if len(password) < 8:
        return False
    else:
        letters_up = [1 for l in password if l.isupper()]
        if len(letters_up) == 0:
            return False
        else:
            number_list = [1 for n in numbers for i in password if n == i]
            if len(number_list) < 3:
                return False
    return True


numbers = '1234567890'

while True:
    password = input('Придумайте пароль: ')
    answer = number_count(password, numbers)
    if answer == False:
        print('Пароль ненадёжный. Попробуйте ещё раз.')
    else:
        print('Это надёжный пароль!')
        break
