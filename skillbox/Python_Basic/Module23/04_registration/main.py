def name_check(person):
    try:
        if not person[0].isalpha():
            raise NameError
    except NameError:
        with open('registrations_bad.log', 'a') as registrations_bad:
            registrations_bad.write(' '.join(person) + '    Поле имени содержит НЕ только буквы: NameError.\n')
    else:
        email_check(person)


def email_check(person):
    try:
        end_mail = False
        for i in '.com', '.ru':
            if person[1].endswith(i):
                end_mail = True

        if end_mail == False or person[1].count('@') == 0:
            raise SyntaxError
    except SyntaxError:
        with open('registrations_bad.log', 'a') as registrations_bad:
            registrations_bad.write(' '.join(person) + '    Поле «Имейл» НЕ содержит @ или .(точку): SyntaxError.\n')
    else:
        age_check(person)


def age_check(person):
    try:
        if int(person[2]) > 99 or int(person[2]) < 10:
            raise ValueError
    except ValueError:
        with open('registrations_bad.log', 'a') as registrations_bad:
            registrations_bad.write(
                ' '.join(person) + '    Поле «Возраст» НЕ является числом от 10 до 99: ValueError\n')
    else:
        with open('registrations_good.log', 'a') as registrations_good:
            registrations_good.write(' '.join(person) + '\n')


with open('registrations.txt', 'r') as reg:

    for i in reg:
        try:
            if i.startswith('\n'):
                continue
            person = i.split()
            if len(person) < 3:
                raise IndexError
            else:
                name_check(person)
        except IndexError:
            with open('registrations_bad.log', 'a') as registrations_bad:
                registrations_bad.write(' '.join(person) + '    НЕ присутствуют все три поля: IndexError\n')
