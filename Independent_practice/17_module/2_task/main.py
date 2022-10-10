word = input('Enter word (list): ')
sym = input('Enter symbol: ')

first_list = [w * 2 for w in word]
second_list = [w * 2 + sym for w in word]

print('List of double characters:', first_list)
print('Gluing with an additional symbol:', second_list)