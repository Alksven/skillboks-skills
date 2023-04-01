from abc import ABC, abstractmethod


class Figure(ABC):

    def __init__(self, length: int, width: int, x: int, y: int):
        self.length = length
        self.width = width
        self.x = x
        self.y = y

    def change_position(self, x: int, y: int):
        self.x = x
        self.y = y
        print('Координаты изменены')

    def __str__(self):
        print(f'Координаты {type(self).__name__}: X - {self.x} Y -  {self.y}')
        print(f'Размеры {self.length}, {self.width}')


class ResizeMixin:

    def resize(self, length: int, width: int):
        self.length = length
        self.width = width


class Square(Figure, ResizeMixin):

    def __init__(self, length: int, x: int, y: int):
        super().__init__(length, length, x, y)


class Rectangle(Figure, ResizeMixin):
    pass


a = [Square(1, 2, 3), Rectangle(1, 2, 3, 4)]

for i in a:
    i.__str__()
    new_length = i.length * 2
    new_width = i.width * 2
    i.resize(new_length, new_width)
    i.__str__()
    print()
