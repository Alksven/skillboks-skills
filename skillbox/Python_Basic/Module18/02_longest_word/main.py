text = input('Введите строку: ').split()
counter = ['', 0]

for i in range(len(text)):
    if len(text[i]) == counter[1]:
        continue
    elif len(text[i]) > counter[1]:
        counter[1] = len(text[i])
        counter[0] = text[i]

print('Самое длинное слово: ', counter[0], '\nДлина этого слова:', counter[1])
