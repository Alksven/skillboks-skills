import random

def function(num):
    alp = 'abcdefghijklmnopqrstuvwxyz'
    list_sym = [random.choice(alp) for _ in range(10)]
    print(num, 'list', list_sym)
    return list_sym

def function_index(sym, num):
    index_list = dict()
    for i, n in enumerate(sym):
        index_list[i] = n
    print(num, 'dictionary', index_list)


list_sym_1 = function('1')
list_sym_2 = function('2')

function_index(list_sym_1, '1')
function_index(list_sym_2, '2')