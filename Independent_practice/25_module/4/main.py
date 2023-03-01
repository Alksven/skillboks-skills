import random


class Robot:

    def __init__(self, model):
        self.model = model

    def __str__(self):
        return '{} model {}'.format(self.__class__.__name__, self.model)

    def operate(self):
        print('The robot goes around')


class MilitaryRobot(Robot):

    def __init__(self, model, gun):
        super().__init__(model)
        self.gun = gun

    def operate(self):
        print('Robot {} guards. Activated {}'.format(self.model, self.gun))


class UnderwaterRobot(Robot):
    def __init__(self, model, depth):
        super().__init__(model)
        self.depth = depth

    def operate(self):
        print('Robot {} guards underwater. Current depth {}'.format(
            self.model, self.depth
        ))


class RobotVacuumCleaner(Robot):
    def __init__(self, model):
        super().__init__(model)
        self.box = 0

    def operate(self):
        self.box = random.randint(1, 100)
        print('Robot {} will harvest. Current bag load {}%'.format(
            self.model, self.box
        ))


p1 = MilitaryRobot(model='5466', gun='Machine gun')
p2 = UnderwaterRobot(model='9988', depth=10)
p3 = RobotVacuumCleaner(model='6655')
p3.operate()
