class Example_1:

    def __init__(self):
        self.element = ''

    def __add__(self, one, second):
        return Example_1



class Water():
    def __init__(self):
        self.element = 'Вода'

    def info(self):
        return self.element


class Air:
    def __init__(self):
        self.element = "Воздух"


class Fire:
    def __init__(self):
        self.element = "Огонь"



class Earth:
    def __init__(self):
        self.element = 'Земля'
