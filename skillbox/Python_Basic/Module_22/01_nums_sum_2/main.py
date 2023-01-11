file_number = open('numbers.txt', 'r')
ready_file = open('answer.txt', 'w')
summ = 0
read_file = file_number.read().split()

for i in read_file:
    if i.isdigit():
        summ += int(i)

ready_file.write(str(summ))

ready_file.close()
file_number.close()



