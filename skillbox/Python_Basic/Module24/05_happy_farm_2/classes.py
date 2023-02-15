class Potato:
    states = {
        0: 'Отсутствует',
        1: 'Росток',
        2: 'Зелёная',
        3: 'Зрелая',
        4: 'Сгнила'
    }

    def __init__(self, index):
        self.index = index
        self.state = 0

    def grow(self):
        if self.state == 4:
            print('Картошка {} {} и пропала'.format(self.index, self.states[self.state]))

        elif self.state == 0:
            print('Садовник уничтожил картошку {}'.format(self.index))
            Garden.potato.remove(self)
        if self.state < 3:
            self.state += 1
        self.print_state()

    def print_state(self):
        print('Картошка {} сейчас {}'.format(
            self.index,
            Potato.states[self.state]
        ))


class Garden:

    def __init__(self, count):
        self.potato = [Potato(index) for index in range(1, count + 1)]
        Gardener(self)

    def grow_all(self):
        print('Картошка прорастает')
        for i_potato in self.potato:
            i_potato.grow()





class Gardener:

    def __init__(self, garden_list):
        self.name = 'Василий'
        self.garden = garden_list



