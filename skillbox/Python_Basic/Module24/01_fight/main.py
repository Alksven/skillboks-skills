from general_class import Players
import random

players_1 = Players('Warrior 1')
players_2 = Players('Warrior 2')
count_round = 1
while True:
    select_player = random.randint(1, 2)
    if select_player == 1:
        Players.damage(players_2, players_1)
    else:
        Players.damage(players_1, players_2)
