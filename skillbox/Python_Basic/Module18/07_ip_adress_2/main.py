ip = input('Введите IP: ')
new_ip = []
a = ''

for i in ip:
    if i.isdigit() or i.isalpha():
        a += i
    else:
        if a.isdigit() == False:
            print(a, '— это не целое число.')
            break
        elif int(a) > 255:
            print(a, 'превышает 255.')
            break
        else:
            new_ip.append(a)
            a = ''
            if i != '.':
                print('Адрес — это четыре числа, разделённые точками.')
                break
            else:
                new_ip.append(i)
else:
    print('IP-адрес корректен.')

print(new_ip)