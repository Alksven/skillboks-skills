class Person:

    __count = 0

    def __init__(self, name, age):
        self.__name = ''
        self.__age = 0
        self.set_name(name)
        self.set_age(age)
        Person.__count += 1

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if name.isalpha():
            self.__name = name
        else:
            print('Не правильный ввод возраста.')

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if isinstance(age, int) and age in range(0, 100):
            self.__age = age
        else:
            print('Не правильный ввод возраста {}.'.format(self.__name))

    def get_count(self):
        return Person.__count


p1 = Person(name='Вася', age=23)
p2 = Person(name='Женя', age=500)
print(p1.get_name(), p1.get_age(), '\n', p1.get_count())
print(Person._Person__count, 'работает ') #no
print(p2.get_name(), p2.get_age(), '\n', p2.get_count())