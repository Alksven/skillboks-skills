def function():
    for i in pro_dict:
        if i[0] in win_dice and i[1] < win_dice[i[0]]:
            continue
        else:
            win_dice[i[0]] = i[1]


def f_winner():
    for i in range(3):



num_of_pro = int(input('Сколько записей вносится в протокол? '))
pro_dict = dict()
win_dice = dict()

print('Записи (результат и имя):')
for i_pro in range(num_of_pro):
    add_pro = input(f'{i_pro + 1}-я запись: ').split()
    pro_dict[(add_pro[1], int(add_pro[0]))] = i_pro

function()
f_winner()

print(win_dice)

# winners = sorted(pro_dict.items(), key=lambda item: item[1], reverse=True)
#
# for i in range(3):
#     print(f'{i + 1}-е место. {winners[i][0]} ({winners[i][1]})')

# 69485 Jack
# 95715 qwerty
# 95715 Alex
# 83647 M
# 197128 qwerty
# 95715 Jack
# 93289 Alex
# 95715 Alex
# 95715 M
