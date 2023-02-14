class Potato:

    readiness_list = ['No potatoes', 'This potatoes is green', 'This potatoes is ripe', 'This potatoes is ready', 'This potato is rotten']

    def __init__(self, number):
        self.num_potato = number
        self.readiness = 0
        print('{} the potato is planted.'.format(number))
        Garden.potato_list.append(self)

    def info_about_Potato(self):
        print(self.num_potato, '-- Status:', self.readiness_list[self.readiness])

    def potatoes_are_growing(self):
        pass


class Garden:
    potato_list = list()

    def __init__(self):
        self.num_potato = None

    def garden_information(self):
        print(self.num_potato)


    def growing_potatoes(self):
        pass



class Gardener:
    pass