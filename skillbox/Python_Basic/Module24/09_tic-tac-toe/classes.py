class Cell:
    def __init__(self, num):
        self.state = True
        self.num = num


class Board:

    def __init__(self):
        self.cells = list()

    def create(self):
        for i in range(1, 10):
            self.cells.append(Cell(i))

    def print_info(self):
        for i, cell in enumerate(self.cells):
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

    def cell_selection(self):
        num_cell = int(input('\n\n{} "{}" Введи номер клетки от 1 до 9: '.format(self.name, self.sym)))
        if not self.board.cells[num_cell - 1].state:
            while not self.board.cells[num_cell - 1].state:
                num_cell = int(input('Клетка уже занята. Выбери другую клетку: '))

        self.cell.append(num_cell)
        self.board.cells[num_cell - 1].num = self.sym
        self.board.cells[num_cell - 1].state = False

    def win(self):
        winn = 0
        for i in Player.winner:
            for i_2 in self.cell:
                if i_2 in i:
                    winn += 1
                    if winn == 3:
                        print('{} Победитель!'.format(self.name))
                        exit()
            winn = 0