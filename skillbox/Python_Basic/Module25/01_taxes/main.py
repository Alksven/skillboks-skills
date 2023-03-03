from classes import Car
from classes import Apartment
from classes import CountryHouse


summ_taxes = 0
money = int(input('How many do you have? '))

property_list = [
    Car(int(input('How much is your Car? '))),
    Apartment(int(input('How much is your Apartment? '))),
    CountryHouse(int(input('How much is your Country House? ')))
]

for property in property_list:
    print(property, property.tax_calculation())
    summ_taxes += property.tax_calculation()

print('\nYour tax: ', round(summ_taxes, 2))
if summ_taxes <= money:
    print('You can pay taxes.')
else:
    print("You can't buy taxes.")