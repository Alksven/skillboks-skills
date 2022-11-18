import math

radius_in = int(input("Enter radius: "))
height_in = int(input("Enter height: "))

def cylinder_math(r, h):
    side = 2 * math.pi * r * h
    full = side + 2 * math.pi * r ** 2
    return side, full


bot_area, full_area = cylinder_math(radius_in, height_in)
print(bot_area, full_area)