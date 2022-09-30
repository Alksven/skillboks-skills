goods = [["яблоки", 50], ["апельсины", 190], ["груши", 100], ["нектарины", 200], ["бананы", 77]]
new_list_fruit = []

print('Current range:', goods)

new_fruit = input('New fruit: ')
new_list_fruit.append(new_fruit)

price = int(input('Price:'))
new_list_fruit.append(price)

goods.append(new_list_fruit)
print('New assortment:', goods)

for i_price in range(len(goods)):
    goods[i_price][1] += goods[i_price][1] / 100 * 8

print('New assortment with increased price:', goods)