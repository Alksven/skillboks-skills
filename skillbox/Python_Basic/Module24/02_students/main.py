from classes import Student

def function(student):
    name = (f'{student[0]} {student[1]}')
    group = int(student[2])
    grade = student[3:]
    return name, group, grade

stud_list = list()

with open('student_list.txt', 'r') as student_list:
    for i, info_stud in enumerate(student_list):
        name, group, grade = function(info_stud.split())
        stud_list.append(Student(f'{name}', group, grade))

ready_stud_list = sorted(stud_list, key=lambda x: x.grade, reverse=True)

for i in range(len(ready_stud_list)):
    ready_stud_list[i].sorted()