def get_input_parameters():

    all_films = int(input('Сколько фильмов хотите добавить? '))
    add_films_list = []

    for count in range(all_films):
        film = input('Введите название фильма: ')
        add_films_list.append(film)

    return add_films_list


def display_result(favorite_films, errors):

    for i_error in errors:
        print(f'Ошибка: фильма {i_error} у нас нет :(')
    print('Ваш список любимых фильмов:', end=' ')

    for i_favorit in favorite_films:
        print(i_favorit, end= ' ')


def add_favorite_film(new_favorite_films, available_films):

    new_list = []
    error_list = new_favorite_films

    for i_film, n_film in enumerate(new_favorite_films):
        for i_available_films in available_films:
            if n_film == i_available_films:
                new_list.append(n_film)
                error_list.remove(new_favorite_films[i_film])
                break

    return new_list, error_list


if __name__ == '__main__':
    available_films = ["Крепкий орешек", "Назад в будущее", "Таксист", "Леон", "Богемская рапсодия", "Город грехов", "Мементо", "Отступники", "Деревня"]
    new_favorite_films = get_input_parameters()
    favorite_films, errors = add_favorite_film(new_favorite_films, available_films)
    display_result(favorite_films, errors)