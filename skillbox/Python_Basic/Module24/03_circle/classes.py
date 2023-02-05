class Circle:
    circles_list = []

    def __init__(self, num_circle, x=0, y=0, r=6):
        self.num_circle = num_circle
        self.x = x
        self.y = y
        self.r = r
        self.circles_list.append([self.num_circle, self.x, self.y, self.r])
        print('{} created'.format(num_circle))


    def circle_area(self):
        s = 3.14 * (self.r ** 2)
        print(self.r)
        print('Площадь круга = {}'.format(s))
