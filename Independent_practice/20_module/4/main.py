text = input('Enter text: ')
index_list = ''

for i, sum in enumerate(text):
    if sum == '~':
        index_list += str(i)

print('Answer:', ' '.join(index_list))