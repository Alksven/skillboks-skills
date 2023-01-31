def count_words_letters(txt):
    new_text = ''
    for i in txt:
        for i_2 in i:
            if i_2.isalpha() or i_2 == ' ':
                new_text += i_2.lower()

    word = new_text.split()
    letter = new_text.replace(' ', '')
    min_let = [min(letter), letter.count(min(letter))]

    return len(word), len(letter), min_let


text = open('zen.txt', 'r')

summ_str = [i.strip() for i in text]

num_words, num_letters, letter_min = count_words_letters(summ_str)

print('Количество букв в файле: ', num_letters)
print('Количество слов в файле: ', num_words)
print('Количество строк в файле: ', len(summ_str))
print(f'Наиболее редкая буква: "{letter_min[0]}" встречается {letter_min[1]} раз(a)')
text.close()
