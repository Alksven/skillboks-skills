def cut(text):
    text.append(' ')
    new_text = []
    count = 1
    for l in range(len(text) - 1):
        if text[l] == text[l + 1]:
            count += 1
        else:
            new_text.append(text[l] + str(count))
            count = 1
    return new_text


text = list(input('Введите строку: '))

cut_text = cut(text)
print(''.join(cut_text))
