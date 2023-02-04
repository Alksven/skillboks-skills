class Student:
    list_students = []
    def __init__(self, name, group, grade):
        self.name_surname = name
        self.num_group = group
        self.grade = Performance.gpa(grade, grade)
        self.list_students.append([self.name_surname, self.num_group, self.grade])


class Performance():
    def gpa(self, grade):
        summ_grade = 0
        for i in grade:
            summ_grade += int(i)
        performance = summ_grade / 5
        return performance

class Sort():

    def sorted(self, list_stud):
        ready_sort_list = sorted(list_stud, key=lambda x: x[2], reverse=True)
        for i in ready_sort_list:
            print(*i)
