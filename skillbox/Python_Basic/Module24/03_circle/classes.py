import math
class Circle:
    PI = math.pi

    def __init__(self, num_circle, x, y, r):
        self.num_circle = num_circle
        self.x = x
        self.y = y
        self.r = r
        print(self.num_circle, 'Создан круг')

    def circle_area(self):
        s = self.PI * (self.r ** 2)
        print('Площадь круга = {}'.format(s))

    def circle_perimeter(self):
        c = 2 * self.PI * self.r
        print('Периметр круга = {}'.format(c))

    def enlarge_circle(self):
        add_size = int(input('Во сколько раз увеличить круг? '))
        self.r = self.r * add_size
        print('Новый радиус круга = {}'.format(self.r))

    def intersections(self, old_x, old_y, old_r, num_old_circle):
        hypotenuse = (abs(self.x - old_x) ** 2) + (abs(self.y - old_y) ** 2)
        summ_r = self.r + old_r
        print(hypotenuse)
        print(summ_r)
        if summ_r >= math.sqrt(hypotenuse):
            print('Круг пересекается с кругом {}'.format(num_old_circle))
        else:
            print('Круг не пересекается с кругом {}.'.format(num_old_circle))



