numbers = int(input('How many numbers will be in the list? '))
numbers_list = []
summ_i = 0
for count in range(1, numbers + 1):
    print(f'Enter {count} number', end=' ')
    number = int(input())
    numbers_list.append(number)

divide = int(input('Enter divide '))

for i_count in range(numbers):
    if numbers_list[i_count] % divide == 0:
        print(f'index {numbers_list[i_count]} = {i_count}')
        summ_i += i_count
print(f'Sum of index = {summ_i}')

