violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]
time_list = 0
count_song = int(input('Сколько песен выбрать? '))

for i_count in range(count_song):
    print(f'Название {i_count + 1}-й песни: ', end=' ')
    song = input()

    for i_list in range(len(violator_songs)):
        if song == violator_songs[i_list][0]:
            time_list += violator_songs[i_list][1]

print('Общее время звучания песен:', round(time_list, 2), 'минуты')
