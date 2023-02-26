class Cell:
    def __init__(self, num):
        self.state = True
        self.num = num


    #  Клетка, у которой есть значения
    #   - занята она или нет
    #   - номер клетки


class Board:

    def __init__(self):
        self.board_1 = list()

    def create(self):
        for i in range(1, 10):
            self.board_1.append(Cell(i))


    def print_info(self):
        for i, cell in enumerate(self.board_1):
            if i % 3 == 0:
                print()
            print(cell.num, end='  \t')


class Player:

    winner = [[1, 2, 3], [1, 5, 9], [3, 5, 7], [4, 5, 6], [2, 5, 8], [3, 6, 9], [1, 4, 7], [7, 8, 9]]
    def __init__(self, name, board, sym):
        self.name = name
        self.cell = list()
        self.board = board
        self.sym = sym

    def add_cell(self, num_cell):
        if not self.board.board_1[num_cell - 1].state:
            return print('Клетка уже занята')
        else:
            self.cell.append(num_cell)
            self.board.board_1[num_cell - 1].num = self.sym
            self.board.board_1[num_cell - 1].state = False


    def win(self):
        if self.cell.sort() in Player.winner:
            print('{} победил.'.format(self.name))
        else:
            for i in range(1, len(self.cell)):
                if self.cell.sort()[i:] in Player.winner:




    #  У игрока может быть
    #   - имя
    #   - на какую клетку ходит