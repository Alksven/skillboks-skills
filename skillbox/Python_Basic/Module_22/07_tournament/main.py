first_tour = open('first_tour.txt', 'r')
all_people = list()
winner_list = dict()

for i, str_1 in enumerate(first_tour):
    all_people.append(str_1.split())

for i_2 in range(1, len(all_people)):
    if int(all_people[i_2][2]) > int(all_people[0][0]):
        winner_list[i_2] = [all_people[i_2][1][0] + '.', all_people[i_2][0], int(all_people[i_2][2])]       # составляем список в нужнопм порядке значений


second_tour = open('second_tour.txt', 'a')
second_tour.write(str(len(winner_list)) + '\n')

for i_3, nb in enumerate(sorted(winner_list.values(), key=lambda x: x[2], reverse=True)):        #отсортированный список по местам
    second_tour.write(str(i_3 + 1) + ') ' + " ".join(map(str, nb)) + '\n')      #записываем файл 2 тура

first_tour.close()
second_tour.close()



