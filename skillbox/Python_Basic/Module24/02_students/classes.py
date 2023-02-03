class Student:

    def __init__(self, name, group, grade):
        self.name_surname = name
        self.num_group = group
        self.grade = grade
        print(self.name_surname)

    def performance(self):
        summ_grade = 0
        for i in self.grade:
            summ_grade += int(i)
        self.performance = summ_grade // 5
        print(self.performance)

    def print_info(self):
        print(self.name_surname)
        print(self.num_group)
        print(self.grade)
        print(self.performance)
