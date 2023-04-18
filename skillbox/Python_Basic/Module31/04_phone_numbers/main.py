import re

numbers = ['9999999999', '999999-999', '99999x9999']
pattern_num = r'\b\d[89]\d{8}\b'
for i, num in enumerate(numbers):
    if re.search(pattern_num, num):
        print(f'{i + 1} номер: всё в порядке')
    else:
        print(f'{i + 1} номер: не подходит')