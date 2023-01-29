from general_class import Fight
import random

player_1 = Fight('1')
player_2 = Fight('2')

while player_1.health != 0 or player_2.health != 0:
    select_player = random.random()