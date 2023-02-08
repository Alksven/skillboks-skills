class Players:

    def __init__(self, player, health=100):
        self.name_player = player
        self.health = health

    def damage(self, attack_player):
        self.health -= 20
        print('Beats {}. The {} has {}% health.'.format(
            attack_player.name_player, self.name_player, self.health))
        if self.health <= 0:
            print('The {} wins.'.format(attack_player.name_player))
            exit()
