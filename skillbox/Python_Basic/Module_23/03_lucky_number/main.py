import random

summ_num = 0

with open('out_file.txt', 'a') as out_file:
    while summ_num < 777:
        try:
            number = int(input('Введите число: '))
            random_number = random.randint(0, 100)
            if random_number <= 13:
                raise BaseException
            summ_num += number
            out_file.write(str(number) + '\n')

        except BaseException:
            print('Вас постигла неудача!')
            break
    else:
        print('Вы успешно выполнили условие для выхода из порочного цикла!')
