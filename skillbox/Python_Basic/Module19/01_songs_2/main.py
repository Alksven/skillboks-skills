violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

num_songs = int(input('Сколько песен выбрать? '))
time_songs = 0

for count in range(num_songs):
    name = input('Название песни: ')
    if name in violator_songs:
        time_songs += violator_songs[name]
    else:
        print('Такой песни нет!')

print('Общее время звучания песен: {0} минуты'.format(time_songs))