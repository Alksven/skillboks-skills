word_list = []
count = [0, 0, 0]

for count_word in range(3):
    print(f'Enter {count_word + 1} word', end=' ')
    word = input()
    word_list.append(word)

text = input('\nEnter text: ')
while text != 'end':
    for index in range(3):
        if word_list[index] == text:
            count[index] += 1
    text = input('Enter text: ')

print('\nWord count in text')
for i in range(3):
    print(word_list[i], ':', count[i])