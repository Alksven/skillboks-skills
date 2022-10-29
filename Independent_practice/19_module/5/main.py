incomes = {
    'apple': 5600.20,
    'orange': 3500.45,
    'banana': 5000.00,
    'bergamot': 3700.56,
    'durian': 5987.23,
    'grapefruit': 300.40,
    'peach': 10000.50,
    'pear': 1020.00,
    'persimmon': 310.00,
}

all_income = sum(incomes.values())
product_min = [x for x, y in incomes.items() if y == min(incomes.values())][0]


print('The total income for the year amounted to {0} rubles'.format(all_income))
print('{0} have the smallest income. It is {1} rubles'.format(product_min, min(incomes.values())))
incomes.pop(product_min)
print('Final dictionary:', incomes)
