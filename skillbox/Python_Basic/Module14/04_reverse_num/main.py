def func(number):
    number_help = str(number)
    whole = ''
    part = ''
    answer = ''
    for count in number_help:
        if count == '.':
            whole = part
            part = ''
            continue
        part += count

    whole = int(whole)
    part = int(part)

    while whole != 0:
        answer += str(whole % 10)
        whole //= 10
    answer += '.'
    while part != 0:
        answer += str(part % 10)
        part //= 10
    return float(answer)


number_first = float(input('Введите первое число: '))
number_second = float(input('Введите второе число: '))

number_first_summ = func(number_first)
print('Первое число наоборот:', number_first_summ)

number_second_summ = func(number_second)
print('Второе число наоборот:', number_second_summ)

print('Сумм:', number_first_summ + number_second_summ)
