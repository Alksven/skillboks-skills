def fun(task):
    try:
        a, sym, b = task.split()
        if len(sym) != 1:
            raise BaseException
    except BaseException:
        print(f'Обнаружена ошибка в строке: {i[0:len(i) - 1]} Хотите исправить?')
    else:
        if sym == '+':
        if sym == '-':
        if sym == '*':
        if sym == '/':
        if sym == '//':
        if sym == '**':



summ = 0
with open('calc.txt', 'r') as cals:

    for i in cals:
         answer_task = fun(i)
         summ += answer_task









