last_num = int(input('Введие число: '))

squares = (x ** 2 for x in range(1, last_num + 1))
count = 1

for i in squares:
    print(count, ' = ', i)
    count += 1