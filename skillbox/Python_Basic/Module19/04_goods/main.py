goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

def calculation(product,dict_store):
    quantity = 0
    price = 0
    count = 0
    for _ in dict_store:
        quantity += dict_store[count]['quantity']
        price += dict_store[count]['price'] * dict_store[count]['quantity']
        count += 1
    print(f'{product} — {quantity} штук, стоимость {price} рубля')




for product in goods:
    quantity = calculation(product, store[goods[product]])


