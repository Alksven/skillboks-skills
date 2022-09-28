def is_film_exist(movie, films_list):
    for i_movie in films_list:
        if i_movie == movie:
            return True
    return False




films = [

    'Крепкий орешек', 'Назад в будущее', 'Таксист',

    'Леон', 'Богемская рапсодия', 'Город грехов',

    'Мементо', 'Отступники', 'Деревня',

    'Проклятый остров', 'Начало', 'Матрица'

]

my_list_films = []
new_movie = ''
while new_movie != 'exit':
    print('Your current top films:', my_list_films)
    new_movie = input('Enter movie name: ')
    if is_film_exist(new_movie, films):
        commands = input('add, insert, remove\nEnter the command: ')
        if commands == 'add':
            my_list_films.append(new_movie)
        if commands == 'remove':
            if is_film_exist(new_movie, my_list_films):
                my_list_films.remove(new_movie)
            else:
                print('There is no such film in our rating.')
        if commands == 'insert':
            index = int(input('to what place? '))
            my_list_films.insert(index - 1, new_movie)
    else:
        print('There is no such movie on the site.')

