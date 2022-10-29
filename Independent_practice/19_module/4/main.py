small_storage = {
    'гвозди': 5000,
    'шурупы': 3040,
    'саморезы': 2000
}

big_storage = {
    'доски': 1000,
    'балки': 150,
    'рейки': 600
}

big_storage.update(small_storage)
print(big_storage)

product = input('Enter Product: ')


if big_storage.get(product) == None:
    print('This item is not in stock.')
else:
    print(big_storage.get(product))