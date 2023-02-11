class Parent:
    parents_list = list()

    def __init__(self, name, age):
        self.name = name
        self.age = int(age)
        self.children_list = list()
        Parent.parents_list.append(self)

    def tell_about_yourself(self):
        print("Меня зовут {}, мне {} лет. ".format(self.name, self.age))
        if len(self.children_list) == 0:
            print('У меня нет детей.')
        else:
            print("Мои дети:")
            for i in range(len(self.children_list)):
                print(self.children_list[i].name, self.children_list[i].age, 'лет.')

    def comfort_children(self, child):
        action = input('{} успокоить ребенка?'.format(self.name)).lower()
        if action == 'да':
            child.calm = True
        else:
            while action != 'да':
                action = input('{} орет! Успокоить? '.format(child.name)).lower()
            child.calm = True

    def feeding_children(self, child):
        action = input('{} покормить ребенка? '.format(self.name)).lower()
        if action == 'да':
            child.hungry = True
        else:
            while action != 'да':
                action = input('{} орет! Накормить? '.format(child.name)).lower()
            child.hungry = True



class Child:
    calm = True
    hungry = True
    children = list()

    def __init__(self, name, age):
        self.name = name
        self.age = int(age)
        self.parent = []
        Child.children.append(self)

    def state_calm(self):
        print('{} начал(а) вредничать.'.format(self.name))
        self.calm = False
        self.parent[0].comfort_children(self)

    def state_hungry(self):
        print('{} проголодался.'.format(self.name))
        self.calm = False
        self.parent[0].feeding_children(self)