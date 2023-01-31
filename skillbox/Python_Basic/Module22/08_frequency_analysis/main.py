def get_clean_text(text):
    all_letters = ''
    for i_str in text:
        for i_let in i_str:
            if i_let.isalpha():
                all_letters += i_let.lower()
    return all_letters


text = open('text.txt', 'r')
count_letters = list()

all_text = get_clean_text(text)

sym_perc = set(all_text)

for letter in sym_perc:
    count_letters.append([letter, round(all_text.count(letter) / len(all_text), 3)])

count_letters = sorted(count_letters, key=lambda l: l[0])
count_letters = sorted(count_letters, key=lambda i: i[1], reverse = True)

analysis = open('analysis.txt', 'w')
for i in count_letters:
    analysis.write(" ".join(map(str, i)) + '\n')

text.close()
analysis.close()

