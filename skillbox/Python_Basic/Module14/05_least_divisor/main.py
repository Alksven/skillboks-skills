number = int(input('ВВведите число: '))
for count in range(2, number + 1):
    if number % count == 0:
        print('Наименьший делитель, отличный от единицы:', count)
        break
