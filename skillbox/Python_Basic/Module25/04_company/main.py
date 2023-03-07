from classes import Manager
from classes import Agent
from classes import Worker

employees = [
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

for employee in employees:
        employee.calculate_salary()
        print(employee)