dict_country = dict()

num_of_country = int(input('Количество стран: '))

for count in range(num_of_country):
    country_and_city = input(f'{count + 1} страна: ').split()
    for i_city in range(len(country_and_city), 0, -1):
        dict_country[country_and_city[i_city]] = country_and_city[0]

# for search_city in range(1, 4):
#     city = input(f'Введите город {search_city}: ')

print(dict_country)


# Россия Москва Петербург Новгород
# Германия Берлин Лейпциг Мюнхен

