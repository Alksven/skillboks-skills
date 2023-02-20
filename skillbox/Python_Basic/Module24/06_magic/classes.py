
class Water():
    def __init__(self, num):
        self.element = 'Вода'
        self.num = num

    def __add__(self, other):
        return Water(self.num + other.num)


class Air:
    def __init__(self, num):
        self.element = "Воздух"
        self.num = num

    def __add__(self, other):
        return Air(self.num + other.num)


class Fire:
    def __init__(self, num):
        self.element = "Огонь"
        self.num = num

    def __add__(self, other):
        return Fire(self.num + other.num)

class Earth:
    def __init__(self, num):
        self.element = 'Земля'
        self.num = num

    def __add__(self, other):
        return Earth(self.num + other.num)