def encryption(letters, sentence, step):

    answer = []
    for l in sentence:
        if letters.count(l) == 0:
            answer.append((l))
            continue
        if letters.index(l) + step >= len(letters):
            answer.append(letters[letters.index(l) - len(letters) + step])
        else:
            answer.append(letters[letters.index(l) + step])

    return answer


letters = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
           'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

sentence = input('Введите сообщение: ').lower()
step = int(input('Введите сдвиг: '))

secret_sentence = encryption(letters, sentence, step)

print(''.join(secret_sentence))