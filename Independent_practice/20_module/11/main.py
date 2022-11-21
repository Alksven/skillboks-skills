contact_list = dict()
add_contact = input('Enter the last name first name separated by a space: ').split()

while add_contact[0] != '0':
    contact_list[(add_contact[0], add_contact[1])] = int(add_contact[2])
    add_contact = input('Enter the last name first name separated by a space: ').split()


print('Entry completed\n', contact_list)
