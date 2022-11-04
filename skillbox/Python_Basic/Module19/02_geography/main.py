
dict_country = dict()

num_of_country = int(input('Количество стран: '))

for count in range(num_of_country):
    country_and_city = input(f'{count + 1} страна: ').split()
    dict_country[country_and_city[0]] = country_and_city[1:]


for search_city in range(1, 4):
    city = input(f'Введите город {search_city}: ')
    for i in dict_country.values():
        if city == i:
            print('asdf')


print(dict_country)

# city = input('Первый город: ')
# print()

# Россия Москва Петербург Новгород
# Германия Берлин Лейпциг Мюнхен

