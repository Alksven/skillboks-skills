class Unit:

    def __init__(self):
        self.health = 100

    def damage(self, damage):
        self.health -= 0

    def __str__(self):
        return 'Unit: {}. health: {}.'.format(self.__class__.__name__, self.health)


class Soldier(Unit):

    def __init__(self):
        super().__init__()

    def damage(self, damage):
        self.health -= damage


class CivilianMan(Unit):
    def __init__(self):
        super().__init__()

    def damage(self, damage):
        self.health -= damage * 2
