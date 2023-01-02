import os

file = open('/home/ven/my_projects/task/group_1.txt', 'r')
summa = 0

for i_line in file:
    info = i_line.split()
    summa += int(info[2])

file = open('/home/ven/my_projects/task/group_1.txt', 'r')
diff = 0

for i_line in file:
    info = i_line.split()
    diff -= int(info[2])

file.close()

file_2 = open('/home/ven/my_projects/task/Additional_info/group_2.txt', 'r')
compose = 1

for i_line_2 in file_2:
    info = i_line_2.split()
    compose *= int(info[2])

file_2.close()

print(summa)
print(diff)
print(compose)