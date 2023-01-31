first_tour = open('first_tour.txt', 'r')
all_people = list()
winner_list = dict()

for _, data in enumerate(first_tour):
    all_people.append(data.split())

for i in range(1, len(all_people)):
    if int(all_people[i][2]) > int(all_people[0][0]):
        winner_list[i] = [all_people[i][1][0] + '.', all_people[i][0], int(all_people[i][2])]

second_tour = open('second_tour.txt', 'a')
second_tour.write(str(len(winner_list)) + '\n')

for num_win, win in enumerate(sorted(winner_list.values(), key=lambda x: x[2], reverse=True)):
    second_tour.write(str(num_win + 1) + ') ' + " ".join(map(str, win)) + '\n')

first_tour.close()
second_tour.close()
