class Person:

    def __init__(self, surname, name, age):
        self.__surname = surname
        self.__name = name
        self.__age = age



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
        return f'Surname: {self.__surname}: Name: {self.__name}. Age: {self.__age}. Salary: {self.salary}'


class Agent(Employee, Person):

    def __init__(self, surname, name, age, sales):
        super().__init__(surname, name, age)
        self.sales = sales
        self.salary = 0


    def calculate_salary(self):
        self.salary = 5000 + (self.sales / 100 * 5)

    def __str__(self):
        return f'Surname: {self.__surname}: Name: {self.__name}. Age: {self.__age}. Salary: {self.salary}'


class Worker(Employee, Person):

    def __init__(self, surname, name, age, hours):
        super().__init__(surname, name, age)
        self.hours = hours
        self.salary = 0


    def calculate_salary(self):
        self.salary = 100 * self.hours

    def __str__(self):
        return f'Surname: {self.__surname}: Name: {self.__name}. Age: {self.__age}. Salary: {self.salary}'


employee = [
        Manager(surname='Петров', name="Женя", age=34),
        Manager(surname="Иванов", name="Вова", age=25),
        Manager(surname="Сидоров", name="Валентин", age=20),
        Agent(surname="Пилецкий", name="Алексендр", age=35, sales=1000000),
        Agent(surname="Никрасов", name="Олег", age=27, sales=650000),
        Agent(surname="Мироненко", name="Юлия", age=30, sales=345000),
        Worker(surname="Князева", name="Светлана", age=18, hours=120),
        Worker(surname="Алексеев", name="Руслан", age=33, hours=80),
        Worker(surname="Ганиев", name="Ринат", age=39, hours=50)
]

for i in employee:
        i.calculate_salary()
        print(i)