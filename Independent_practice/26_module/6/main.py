def gen(num_list):
    for i in num_list:
        b = i.split()
        for i_2 in b:
            yield int(i_2)


summ = 0
with open('number.txt', 'r') as num_list:
    for i in gen(num_list):
        summ += i

print(summ) 