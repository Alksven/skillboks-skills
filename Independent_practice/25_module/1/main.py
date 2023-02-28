class Point:
    __count = 0

    def __init__(self, x=0, y=0):
        self.set_x(x)
        self.set_y(y)
        self.__count += 1

    def __str__(self):
        return 'X = {}\nY = {}'.format(self.__x, self.__y)

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def set_x(self, x):
        if isinstance(x, int):
            self.__x = x
        else:
            raise Exception('X не число')

    def set_y(self, y):
        if isinstance(y, int):
            self.__y = y
        else:
            raise Exception('Y не число')


first_dot = Point(2, 3)
print(first_dot)
