a = int(input('Enter A: '))
b = int(input('Enter B: '))
ab_list = [x for x in range(a, b + 1) if x % 2 == 0]
print(ab_list)