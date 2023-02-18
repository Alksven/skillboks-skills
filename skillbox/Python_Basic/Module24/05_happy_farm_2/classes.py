class Gardener:

    def __init__(self, name, garden):
        self.name = name
        self.job = garden
        self.harvest_1 = []

    def care(self):
        print('{} полил картошку.\n'.format(self.name))
        Garden.grow_all(self.job)

    def harvest(self):
        for i in self.job.potato:
            print('{} собрал картошку {}'.format(self.name, i.index))
            self.harvest_1.append(i.index)


class Potato:
    states = {
        0: 'Отсутствует',
        1: 'Росток',
        2: 'Зелёная',
        3: 'Зрелая',
    }

    def __init__(self, index):
        self.index = index
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    def print_state(self):
        print('Картошка {} сейчас {}'.format(self.index, Potato.states[self.state]
                                             ))

    def is_ripe(self):
        if self.state == 3:
            return True
        return False


class Garden:

    def __init__(self, count_potato):
        self.potato = [Potato(index) for index in range(1, count_potato + 1)]

    def grow_all(self):
        print('\nКартошка прорастает')
        for i_potato in self.potato:
            i_potato.grow()

    def are_all_ripe(self):
        if not all([i_potato.is_ripe() for i_potato in self.potato]):
            print('\nКартошка еще не созрела\n')
        else:
            print("Картошка вся созрела. Можно собирать\n")
            return True
