class Person:

    def __init__(self, surname, name, age):
        self._surname = surname
        self._name = name
        self._age = age



class Employee(Person):

    def calculate_salary(self):
        pass


class Manager(Employee, Person):
    def __init__(self, surname, name, age):
        super().__init__(surname, name, age)
        self.salary = 0

    def calculate_salary(self):
        self.salary = 13000

    def __str__(self):
        return f'Surname: {self._surname}. Name: {self._name}. Age: {self._age}. Salary: {self.salary}'


class Agent(Employee, Person):

    def __init__(self, surname, name, age, sales):
        super().__init__(surname, name, age)
        self.sales = sales
        self.salary = 0


    def calculate_salary(self):
        self.salary = 5000 + (self.sales / 100 * 5)

    def __str__(self):
        return f'Surname: {self._surname}. Name: {self._name}. Age: {self._age}. Salary: {self.salary}'


class Worker(Employee, Person):

    def __init__(self, surname, name, age, hours):
        super().__init__(surname, name, age)
        self.hours = hours
        self.salary = 0


    def calculate_salary(self):
        self.salary = 100 * self.hours

    def __str__(self):
        return f'Surname: {self._surname}. Name: {self._name}. Age: {self._age}. Salary: {self.salary}'
