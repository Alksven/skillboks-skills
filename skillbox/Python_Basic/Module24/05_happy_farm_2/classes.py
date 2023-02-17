import random


class Gardener:

    def __init__(self, name, garden):
        self.name = name
        self.gardener_state = True
        self.job = garden

    def drink_gardener(self):
        state = random.randint(0, 1)
        if state == 0:
            self.gardener_state = False
        else:
            self.gardener_state = True
        self.care()

    def care(self):
        choice_potato = random.randint(0, len(self.job.potato))
        if self.gardener_state == False:
            print('{} сегодня выпил и упал на картошку {} и повредил ее.'.format(
                self.name,
                self.job.potato[choice_potato].index))
            Potato.step_back(self.job.potato[choice_potato])
        else:
            print('{} сегодня трезвый. Он полил картошку {}'.format(
                self.name,
                self.job.potato[choice_potato].index))
            Potato.grow(self.job.potato[choice_potato])



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



    def step_back(self):
        self.state -= 1


    def print_state(self):
        print('Картошка {} сейчас {}'.format(self.index, Potato.states[self.state]
        ))



class Garden:

    def __init__(self, count_potato):
        self.potato = [Potato(index) for index in range(1, count_potato + 1)]

    def grow_all(self):
        print('Картошка прорастает')
        for i_potato in self.potato:
            i_potato.grow()


    def delete(self):
        if self.potato[].state == 4:
            print('WARNING: Картошка {} {} и пропала'.format(self.index, self.states[self.state]))
        elif i.state == 0:
            print('WARNING: Садовник уничтожил картошку {}'.format(i.index))
            self.potato.remove(i)


