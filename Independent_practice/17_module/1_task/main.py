first_number = int(input('Enter number A: '))
second_number = int(input('Enter number B: '))

cube = [a ** 3 for a in range(first_number, second_number + 1)]
square = [a ** 2 for a in range(first_number, second_number + 1)]

print(f'List of cubes of numbers ranging from {first_number} to {second_number}: {cube}')
print(f'List of squared numbers ranging from {first_number} to {second_number}: {square}')