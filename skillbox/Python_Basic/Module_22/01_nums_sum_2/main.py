file_number = open('numbers.txt', 'r')
ready_file = open('answer.txt', 'w')
summ = 0

del_sym = [i.strip() for i in file_number]
for i in del_sym:
    if i.isdigit():
        summ += int(i)

ready_file.write(str(summ))

ready_file.close()
file_number.close()



