def square(num):
    for i in range(1, num + 1):
        print(i, end=' = ')
        yield i ** 2


last_num = int(input('Введие число: '))
square = square(last_num)

for i in square:
    print(i)