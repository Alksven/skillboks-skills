from classes import Player
from classes import Board
import random


board = Board()
player_1 = Player('Петя', board, 'X')
player_2 = Player('Вася', board, '0')


print('Два игрока:\n{} использует "Х"\n{} использует "0"'.format(player_1.name, player_2.name))
print('Игра началась.')
board.create()
board.print_info()

while True:
    for player in player_1, player_2:
        player.add_cell(int(input('\n\n{} Введи номер клетки от 1 до 9: '.format(player.name))))
        board.print_info()
        if len(player.cell) >= 3:
            player.win()





