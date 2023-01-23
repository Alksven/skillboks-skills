class Point:
    count = 0

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.count += 1


    def info_dot(self):
        print('X =', self.x, '\nY =', self.y)
        print(self.count)

first_dot = Point(2, 3)
first_dot.info_dot()
