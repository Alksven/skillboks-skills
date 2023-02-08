class Student:

    def __init__(self, name, group, grade):
        self.name_surname = name
        self.num_group = group
        self.grade = Student.average_rating(self, grade)

    def average_rating(self, grade):
        summ = 0
        for i in grade:
            summ += int(i)
        return summ / 5

    def sorted(self):
        print('{}....{}   {}'.format(self.name_surname, self.num_group, self.grade))