from classes import MyDict

person = MyDict()

action = 1
while action != 0:
    action = int(input('1 = Add/change element.\n2 = Check element.\n0 = Exit.\nEnter: '))
    if action == 0:
        break
    if action == 1:
        key, value = input('Enter the keys and its value: ').split()
        person.set_element(key=key, value=value)
    if action == 2:
        key = input('Enter the key: ')
        value = person.get_key(key)
        if value == 0:
            print('There is no such key.')
        else:
            print('key value {} = {}.'.format(key, value))