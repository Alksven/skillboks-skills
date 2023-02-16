import random

class Gardener:

    def __init__(self, name):
        self.name = name
        self.gardener_state = True
        self.job = Garden()


    def water_potatoes(self):
        select = random.randint(0, len(self.garden))



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
        if self.state < 3:
            self.state += 1
        self.print_state()


    def print_state(self):
        print('Картошка {} сейчас {}'.format(self.index, Potato.states[self.state]
        ))


class Garden:


    def __init__(self):
        count_potato = int(input('Сколько картошки посадим?'))
        self.potato = [Potato(index) for index in range(1, count_potato + 1)]
        print(self.potato)
        Gardener(self)

    def grow_all(self):
        print('Картошка прорастает')
        for i_potato in self.potato:
            i_potato.grow()
        Garden.delete(self)

    def delete(self):
        for i in self.potato:
            if i.state == 4:
                print('WARNING: Картошка {} {} и пропала'.format(i.index, i.states[i.state]))
                self.potato.remove(i)
            elif i.state == 0:
                print('WARNING: Садовник уничтожил картошку {}'.format(i.index))
                self.potato.remove(i)










