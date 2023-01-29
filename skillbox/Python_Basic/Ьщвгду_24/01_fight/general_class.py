
class Fight:

    def __init__(self, player):
        self.name_player = 'Воин {}'.format(player)
        self.health = 100

    def damage(self, player):
        if player == 0:
            print('Бьет первый воин')
            self.

