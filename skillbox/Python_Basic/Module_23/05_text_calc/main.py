def fun(a, sym, b):
    a = int(a)
    b = int(b)
    if sym == '+':
        return a + b
    elif sym == '-':
        return a - b
    elif sym == '*':
        return a * b
    elif sym == '/':
        return a / b
    elif sym == '//':
        return a // b
    elif sym == '**':
        return a ** b


summ = 0
with open('calc.txt', 'r') as cals:

    for i, task in enumerate(cals):
        try:
            a, sym, b = task.split()
            answer_task = fun(a, sym, b)
            summ += answer_task

        except TypeError:
            print(f'Обнаружена ошибка в строке: {task[0:len(task) - 1]} Хотите исправить?')
            select = input().lower()
            if select == 'да':
                edit = input('Введите исправленную строку: ').split()
                answer_task = fun(edit[0], edit[1], edit[2])
                summ += answer_task

print('Сумма результатов:', summ)






