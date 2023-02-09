class Parent:

    def __init__(self, name, age, children):
        self.name = name
        self.age = age
        self.children = children

    def tell_about_yourself(self):
        pass

    def comfort_children(self):
        pass

    def feeding_children(self):
        pass



class Child:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def state_calm(self):
        pass

    def state_hungry(self):
        pass