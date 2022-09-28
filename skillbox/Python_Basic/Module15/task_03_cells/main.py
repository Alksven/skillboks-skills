def get_input_parameters():

    count_cells = int(input('Количество клеток: '))
    rank_list = []

    for i_cells in range(count_cells):
        print(f'Эффективность {i_cells + 1} клетки', end='')
        rank = int(input())
        rank_list.append(rank)

    return rank_list


def display_result(cells):

    print('Неподходящие значения:', cells)


def select_cells(cells):

    win_cell = []
    for index, cell in enumerate(cells):
        if cell < index:
            win_cell.append(cell)

    return win_cell


if __name__ == '__main__':

    cells = get_input_parameters()
    result_cells = select_cells(cells)
    display_result(result_cells)
