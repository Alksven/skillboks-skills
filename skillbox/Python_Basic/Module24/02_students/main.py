from classes import Student
import random

def function(student):
    name = (f'{student[0]} {student[1]}')
    group = int(student[2])
    grade = student[3:]
    return name, group, grade

a =
with open('student_list.txt', 'r') as student_list:
    for info_stud in student_list:
        name, group, grade = function(info_stud.split())
        Student((f'{name}'), group, grade)
        a.add(locals()[name])

print(a)









# students = [Student(f'Студент_{i}',

# class Student_at:
#
#     def __init__(self, name):
#         self.name = name
#
#
# students = [Student_at(f"Студент_{i}") for i in range(20)]
# for i in range(5):
#     print(f"Объект_{i}: ", students[i])
