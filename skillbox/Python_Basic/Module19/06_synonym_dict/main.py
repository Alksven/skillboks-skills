
num_of_word = int(input('Введите количество пар слов: '))
dict_word = dict()
for i in range(num_of_word):
    word = input(f'{i + 1} пара: ').lower().split()
    dict_word[word[0]] = word[2]
print(dict_word)

search = False
while search != True:
    search_word = input('Введите слово: ')
    if search_word in dict_word.values():
        print('Синоним:', dict_word.keys([search_word]))
        search = True
    else:
        print('Такого слова в словаре нет.')

# Привет — Здравствуйте
# Печально — Грустно
# Весело — Радостно