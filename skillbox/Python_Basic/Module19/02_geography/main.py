dict_country = dict()

num_of_country = int(input('Количество стран: '))

for count in range(num_of_country):
    country_and_city = input(f'{count + 1} страна: ').split()
    for i in range(1, len(country_and_city)):
        dict_country[country_and_city[i]] = country_and_city[0]

for search_city in range(1, 4):
    city = input(f'Введите город {search_city}: ')
    if city in dict_country:
        print(f'Город {city} расположен в стране {dict_country[city]}')
    else:
        print(f'По городу {city} данных нет.')






