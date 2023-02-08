from classes import Circle

def add_circle(count):
    print('Введите параметры круга: {}'.format(count))
    x_point = float(input("x = "))
    y_point = float(input("y = "))
    r_circle = float(input("R = "))
    return x_point, y_point, r_circle



action = '\n1. Найти площадь этого круга.\n2. Найти периметр этого круга.\n3. Увеличивать этот круг.\n' \
         '4. Пересекается ли тот круг с другими.\n5. Добавить еще один круг.\n6. Завершить программу.'

count_circle = 1
circle_dict = dict()
circle_dict[count_circle] = Circle(f'circle_{count_circle}', 0.0, 0.0, 1.0)

while True:
    print(action)
    select_action = int(input('Выберите действие: '))
    if select_action == 1:
        circle_dict[count_circle].circle_area()
    if select_action == 2:
        circle_dict[count_circle].circle_perimeter()
    if select_action == 3:
        circle_dict[count_circle].enlarge_circle()
    if select_action == 4:
        if len(circle_dict) > 1:
            for i in range(1, len(circle_dict)):
                circle_dict[count_circle].intersections(circle_dict[i])
        else:
            print('Вы добавили всего один круг. Нельзя проверить пересечения.')

    if select_action == 5:
        count_circle += 1
        x, y, r = add_circle(count_circle)
        circle_dict[count_circle] = Circle(f'circle_{count_circle}', x, y, r)
    if select_action == 6:
        print('Программа завершена')
        break


