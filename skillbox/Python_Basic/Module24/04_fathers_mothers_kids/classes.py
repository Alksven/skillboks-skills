class Parent:
    parents_list = list()

    def __init__(self, name, age):
        self.name = name
        self.age = int(age)
        self.children_list = list()
        Parent.parents_list.append(self)


    def tell_about_yourself(self):
        print("My name is {} and I am {} years old. ".format(self.name, self.age))
        print("I have {} children.".format(len(self.children_list)))
        for i in range(len(self.children_list)):
            print(self.children_list[i].name, self.children_list[i].age, 'years old.')


    def comfort_children(self):
        pass

    def feeding_children(self):
        pass



class Child:
    calm = True
    hungry = True
    children = list()

    def __init__(self, name, age):
        self.name = name
        self.age = int(age)
        Child.children.append(self)

    def state_calm(self):
        pass

    def state_hungry(self):
        pass