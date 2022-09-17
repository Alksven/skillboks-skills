import math
def search():
    x_one = float(input('Введите координату X: '))
    y_one = float(input('Введите координату Y: '))
    r = float(input('Введите радиус: '))
    hypotenuse = math.hypot(x_one, y_one)
    if hypotenuse <= r:
        print('Монетка где-то рядом')
    else:
        print('Монетки в области нет')
search()