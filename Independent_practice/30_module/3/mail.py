class Person:

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @age.setter
    def age(self, new_age):
        self.age = new_age

    def __repr__(self):
        return f"({self.name}, {self.age})"


a = Person(name='Вова', age=23)
b = Person(name='Иван', age=40)
c = Person(name='Женя', age=30)
d = Person(name='Таня', age=15)

p_list = [a, b, c, d]
print(p_list)
p_list.sort(key=lambda x: x.age)
print(p_list)
p_list.sort(key=lambda x: -x.age)
print(p_list)
