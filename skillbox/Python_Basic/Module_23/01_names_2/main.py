summ_letter = 0
with open('people.txt', 'r') as people:
    for st, name in enumerate(people):
        try:
            length = len(name)
            if name.endswith('\n'):
                length -= 1
            if length < 3:
                raise BaseException

        except BaseException:
            print('Ошибка: менее трёх символов в строке {}.'.format(st + 1))
            with open('errors.log', 'a') as log:
                log.write('ERROR: BaseException ' + str(st + 1) + ' ' + name)
        finally:
            summ_letter += length

print('Общее количество символов:', summ_letter)
