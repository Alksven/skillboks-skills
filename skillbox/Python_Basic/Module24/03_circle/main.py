from classes import Circle


def add_circle():
    print(f'Enter circle coordinates {count_circle}')
    x_point = float(input("x = "))
    y_point = float(input("y = "))
    r_circle = float(input("R = "))
    Circle(f'circle_{count_circle}', x_point, y_point, r_circle)

action = '1. Найти площадь этого круга.\n2. Найти периметр этого круга.\n3. Увеличивать этот круг.\n' \
         '4. Пересекается ли тот круг с другими.\n5. Добавить еще один круг.\n6. Завершить программу.'
count_circle = 1
select_action = 0
Circle(f'circle_{count_circle}')
print(Circle.circles_list)
while select_action != 6:
    print(action)
    select_action = int(input('Выберите действие: '))
    if select_action == 1:
        Circle(f'circle_{count_circle}').circle_area()
    if select_action == 5:
        count_circle += 1
        add_circle()


