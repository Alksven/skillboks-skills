class Potato:

    readiness_list = ['No potatoes', 'The potatoes are green', 'The potatoes are ripe', 'The potatoes are ready']

    def __init__(self, number):
        self.num_potato = number
        self.readiness = 0
        print('{} the potato is planted'.format(number))
        Garden.potato_list.append(self)
    def info_about_Potato(self):
        print(self.num_potato, '-- Status:', self.readiness_list[self.readiness])

    def potatoes_are_growing(self):
        pass


class Garden:
    potato_list = list()
    pass


class Gardener:
    pass