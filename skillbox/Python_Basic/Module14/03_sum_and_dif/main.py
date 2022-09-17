def summ_number(number):
    summ = 0
    while number != 0:
        summ += number % 10
        number //= 10
    return summ


def count_number(number):
    number_count = number
    count = 0
    while number_count != 0:
        number_count //= 10
        count += 1
    return count


number = int(input('Введите число: '))

summ = summ_number(number)

count = count_number(number)

print('Сумма числе ', summ)
print('Количество цифр в числе:', count)
print('Разность суммы и количества цифр:', summ - count)
