first_tour = open('first_tour.txt', 'r')

list_tour = list()
winner = dict()
for i, str in enumerate(first_tour):
    list_tour.append(str.split())

for i_2 in range(1, len(list_tour)):
    if int(list_tour[i_2][2]) > int(list_tour[0][0]):
        winner[i_2] = [list_tour[i_2][1][0] + '.', list_tour[i_2][0], int(list_tour[i_2][2])]


second_tour = open('second_tour.txt', 'a')

ready_list = '{}'.format(len(winner))
p = 1
for i_3, nb in enumerate(sorted(winner.values(), key=lambda x: x[2], reverse=True)):




