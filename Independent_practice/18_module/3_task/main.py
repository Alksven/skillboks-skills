number_list = []

while len(number_list) < 4:
    number = int(input('Enter Number 0-255: '))
    if number < 0 or number > 255:
        print('ERROR. Repeat Enter')
        continue
    number_list.append(number)

ip = '{0}.{1}.{2}.{3}'.format(
    number_list[0],
    number_list[1],
    number_list[2],
    number_list[3]
)
print('IP', ip)