class CanFly:

    def __init__(self):
        self.speed = 0
        self.height = 0

    def take_off(self):
        pass

    def fly(self):
        pass

    def land(self):
        pass

    def __str__(self):
        return '{} height = {}, speed = {}'.format(
            self.__class__.__name__,
            self.height,
            self.speed
        )


class Rocket(CanFly):

    def take_off(self, height=500, speed=1000):
        self.height = height
        self.speed = speed
        print('Rocket is take of')

    def land(self):
        self.height = 0
        self.explosion()

    def explosion(self):
        self.speed = 0
        print('Explosion')


class Butterfly(CanFly):

    def take_off(self, height=1):
        self.height = height
        print('Butterfly is take of')
        self.fly()

    def fly(self, speed=0.5):
        self.speed = speed
        print('Butterfly is fly')




b = Butterfly()
print(b)
b.take_off()
print(b)

print()
a = Rocket()
print(a)
a.take_off()
print(a)
a.land()
print(a)
