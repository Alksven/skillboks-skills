
class Fight:

    def __init__(self, player, health=100):
        self.name_player = 'Warrior {}'.format(player)
        self.health = health

    def info(self):
        print(self.players)
