from classes import Circle

def add_circle():
    print(f'Введите параметры круга: {count_circle}')
    x_point = float(input("x = "))
    y_point = float(input("y = "))
    r_circle = float(input("R = "))
    circle_dict[count_circle] = Circle(f'circle_{count_circle}', x_point, y_point, r_circle)


action = '\n1. Найти площадь этого круга.\n2. Найти периметр этого круга.\n3. Увеличивать этот круг.\n' \
         '4. Пересекается ли тот круг с другими.\n5. Добавить еще один круг.\n6. Завершить программу.'

count_circle = 1
circle_dict = dict()
circle_dict[count_circle] = Circle(f'circle_{count_circle}', 0.0, 0.0, 2.0)

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
                circle_dict[count_circle].intersections(circle_dict[i].x, circle_dict[i].y, circle_dict[i].r, circle_dict[i].num_circle)
        else:
            print('Вы добавили всего один круг. Нельзя проверить пересечения.')

    if select_action == 5:
        count_circle += 1
        add_circle()
    if select_action == 6:
        print('Программа завершена')
        break


