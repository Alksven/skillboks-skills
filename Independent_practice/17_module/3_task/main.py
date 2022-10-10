def get_higher_price(percent, price):
    return round(price + (price / 100 * percent), 2)


products_list = [1.09, 23.56, 57.84, 4.56, 6.78]

percent_first_year = int(input('Upgrade for the first year: '))
percent_second_year = int(input('Upgrade for the second year: '))

first_year = [get_higher_price(percent_first_year, i_price) for i_price in products_list]
second_year = [get_higher_price(percent_second_year, i_price) for i_price in first_year]

print('Sum of prices for each year:', round(sum(products_list), 2),
      round(sum(first_year), 2), round(sum(second_year), 2))
