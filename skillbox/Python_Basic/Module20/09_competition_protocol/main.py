def score_key(a):
    return a[1][0] * 100000000 - a[1][1]


num_of_pro = int(input('Сколько записей вносится в протокол? '))
pro_dict = dict()
win_dice = dict()

print('Записи (результат и имя):')
for i_pro in range(num_of_pro):
    ball, name = input(f'{i_pro + 1}-я запись: ').split()
    ball = int(ball)
    if name in pro_dict:
        if ball > pro_dict[name][0]:
            pro_dict[name][0] = ball
            pro_dict[name][1] = i_pro
    else:
        pro_dict[name] = [ball, i_pro]

scores = list(pro_dict.items())
scores.sort(key=score_key, reverse=True)

print('\nИтоги соревнований: ')

for winner_index in 0, 1, 2:
    print(f'{winner_index + 1} место {scores[winner_index][0]}', end=' ')
    print(f'({scores[winner_index][1][0]})', sep='')
