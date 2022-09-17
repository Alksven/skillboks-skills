start_year = int(input('С какого года считать? '))
finish_year = int(input('До какого года считать? '))
print(f'Годы от {start_year} до {finish_year} с тремя одинаковыми цифрами:')

year_summ = 0
num_1 = ''
num_2 = ''


for year in range(start_year, finish_year + 1):
    year_summ = str(year)
    num_1 = str(year % 10)
    num_2 = str(year // 10 % 10)
    count_num = 0
    count_num_2 = 0
    for count in year_summ:
        if count == num_1:
            count_num += 1
        elif count == num_2:
            count_num_2 += 1

    if count_num == 3 or count_num_2 == 3:
        print(year)