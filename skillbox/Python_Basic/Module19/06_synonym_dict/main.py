
num_of_word = int(input('Введите количество пар слов: '))
dict_word = dict()
for i in range(num_of_word):
    word = input(f'{i + 1} пара: ').lower().split()
    dict_word[word[2]] = word[0]
print(dict_word)

search = False
while search != True:
    search_word = input('Введите слово: ').lower()
    if search_word in dict_word:
        print('Синоним:', dict_word[search_word].capitalize())
        search = True
    else:
        print('Такого слова в словаре нет.')

# Привет — Здравствуйте
# Печально — Грустно
# Весело — Радостно