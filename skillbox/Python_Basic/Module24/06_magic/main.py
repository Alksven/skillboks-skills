from classes import *
import random

def choice(first, second):
    if index == 1:
        return air
    elif index == 2:
        return water
    elif index == 3:
        return fire
    elif index == 4:
        return earth


element = {
        1: Air(),
        2: Water(),
        3: Fire(),
        4: Earth()
}
while True:
    first_element = random.randint(1, 4)
    second_element = random.randint(1, 4)
    choice(first_element, second_element)
