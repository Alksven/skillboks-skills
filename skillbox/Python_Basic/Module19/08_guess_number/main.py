number_max = int(input('Введите максимальное число: '))

ready_list = {str(x) for x in range(number_max + 1)}
print(len(ready_list), number_max)
while True:
    numbers = set(input('Нужное число есть среди вот этих чисел: '))
    if (numbers == set('помогите!')) and len(ready_list) - 1 == number_max:
        print('Вы еще не совершили попытки угадать')
    elif numbers == set('помогите') or numbers == set('помогите!'):
        print('Артём мог загадать следующие числа:', ' '.join(ready_list))
        break
    else:
        answer = input('Ответ Артёма: ').lower()
        if answer == 'да':
            ready_list.intersection_update(numbers)
            print(ready_list)
        elif answer == 'нет':
            ready_list -= numbers
            print(ready_list)


