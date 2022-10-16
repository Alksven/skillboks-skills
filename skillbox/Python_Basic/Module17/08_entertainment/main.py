import random

stick = int(input('Количество палок: '))
stick_list = ['|' for _ in range(stick)]

throw = int(input('Количество бросков: '))

throw_list_down = [random.randint(1, stick) for _ in range(throw)]
throw_list_up = [random.randint(throw_list_down[x], stick) for x in range(throw)]


for a in range(throw):
    for x in range(throw_list_down[a] - 1, throw_list_up[a]):
        stick_list[x] = '.'

print(''.join(stick_list))

