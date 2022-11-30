num_of_pro = int(input('Сколько записей вносится в протокол? '))
pro_dict = dict()
win_sort = set()

print('Записи (результат и имя):')
for i_pro in range(num_of_pro):
    add_pro = input(f'{i_pro + 1}-я запись: ').split()
    win_sort.add(int(add_pro[0]))
    if len(win_sort) > len(pro_dict):
        pro_dict[(int(add_pro[0]), add_pro[1])] = i_pro

win_sort = list(win_sort)
win_sort.sort(reverse=True)

win_list = [n for i in win_sort[0:3] for n in pro_dict if i in n]

for i_win, win in enumerate(win_list):
    print(f'{i_win + 1}-е место. {win[1]} ({win[0]})')





# 69485 Jack
# 95715 qwerty
# 95715 Alex
# 83647 M
# 197128 qwerty
# 95715 Jack
# 93289 Alex
# 95715 Alex
# 95715 M