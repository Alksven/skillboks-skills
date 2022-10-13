letters = ["а", "е", "ё", "у", "о", "и", "э", "ы", "ю", "я", "А", "Е", "Ё", "И", "О", "У", "Ы", "Э", "Ю", "Я"]

sentence = input('Введите текст: ')

answer_list = [i for i in sentence if letters.count(i) == 1]
print(f'Список гласных букв: {answer_list} \nДлина списка: {len(answer_list)}')
