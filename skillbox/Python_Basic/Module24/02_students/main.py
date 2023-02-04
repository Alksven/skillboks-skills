from classes import Student
from classes import Sort


def function(student):
    name = (f'{student[0]} {student[1]}')
    group = int(student[2])
    grade = student[3:]
    return name, group, grade


with open('student_list.txt', 'r') as student_list:
    for info_stud in student_list:
        name, group, grade = function(info_stud.split())
        Student(f'{name}', group, grade)


Sort.sorted(Student.list_students, Student.list_students)


