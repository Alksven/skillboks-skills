contact_dict = dict()

while True:
    print('Current contacts on the phone:', contact_dict)
    name = input('Enter name: ')
    if name in contact_dict:
        print('A contact with the same name already exists.')
        continue
    number = int(input('Enter number: '))
    contact_dict[name] = number