
class Players:

    def __init__(self, player, health=100):
        self.name_player = player
        self.health = health

    def damage(self, hit):
        self.health -= 20
        print('Beats {}. The {} has {}% health.'.format(
            hit, self.name_player, self.health))
        if self.health <= 0:
            print('The {} wins.'.format(hit))
            exit()
