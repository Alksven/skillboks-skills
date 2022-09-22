text = input('Enter text: ')
sym_list = list(text)
answer = []
edit = ';'
count_edit = 0
for count in sym_list:
    if count == ':':
        answer += edit
        count_edit += 1
        continue
    answer += count
print('Edit text ', end='')
for i in answer:
    print(i, end='')
print(f'\nnumber of fixes {count_edit}')

