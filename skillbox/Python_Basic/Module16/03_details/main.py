shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

summ_count_product = 0
summ_price_product = 0
name_product = input('Название детали: ')

for i_count in range(len(shop)):
    if shop[i_count][0] == name_product:
        summ_price_product += shop[i_count][1]
        summ_count_product += 1

print('Кол-во деталей — ', summ_count_product)
print('Общая стоимость — ', summ_price_product)
