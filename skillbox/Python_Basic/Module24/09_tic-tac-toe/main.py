from classes import Player
from classes import Board

board = Board()
player_1 = Player('Петя', board, 'X')
player_2 = Player('Вася', board, '0')

print('Два игрока:\n{} использует "Х"\n{} использует "0"'.format(player_1.name, player_2.name))
print('Игра началась.')
board.create()
board.print_info()

while True:
    for player in player_1, player_2:
        player.cell_selection()
        board.print_info()
        if len(player_1.cell) + len(player_2.cell) == 9:
            print('\nНикто не выиграл.')
            exit()
        elif len(player.cell) >= 3:
            player.win()





