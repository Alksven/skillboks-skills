def function(help_variable):

    if help_variable.isdigit() == False:
        print(help_variable, '— это не целое число.')
        exit()
    elif int(help_variable) > 255:
        print(help_variable, 'превышает 255.')
        exit()
    else:
        return help_variable


ip = input('Введите IP: ')
new_ip = []
help_variable = ''


for i in ip:
    if i.isdigit() or i.isalpha():
        help_variable += i
    else:
        a_list = function(help_variable)
        new_ip.append(a_list)
        help_variable = ''
        if i != '.':
            print('Адрес — это четыре числа, разделённые точками.')
            exit()
        else:
            new_ip.append(i)

a_list = function(help_variable)


print('IP-адрес корректен.')
