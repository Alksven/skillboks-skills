data = {
    (5000, 123456): ('Иванов', 'Василий'),
    (6000, 111111): ('Иванов', 'Петр'),
    (7000, 222222): ('Медведев', 'Алексей'),
    (8000, 333333): ('Алексеев', 'Георгий'),
    (9000, 444444): ('Георгиева', 'Мария')
}

passport = input('Enter number of passport: ').split()
for i in data:
    if int(passport[0]) in i and int(passport[1]) in i:
        print(data[i])
        break
else:
    print('There is no person with such a passport in the database')
