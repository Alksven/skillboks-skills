number_of_packages = int(input('Enter the number of packages: '))

decoding = []
help_package = []
summ_error = 0

for count_package in range(number_of_packages):
    print('Package №', count_package + 1)
    for add_bit in range(4):
        print(add_bit + 1, 'bit:', end=' ')
        package = int(input())
        help_package.append(package)

    if help_package.count(-1) > 1:
        summ_error += 1
        help_package = []

    else:
        decoding.extend(help_package)
        help_package = []
    print()

print('Message received:', decoding)
print('Number of errors in the message:', decoding.count(-1))
print('Number of lost packages:', summ_error)
