from classes import Car
from classes import Bus

choice = int(input('Автобус = 1 или Машина = 2? '))
x = float(input('Enter X: '))
y = float(input('Enter Y: '))
a = int(input('Enter Angle: '))
lis_technology = [Bus(x=x, y=y, a=a), Car(x=x, y=y, a=a)]

while True:
    lis_technology[choice - 1].move()
    print(lis_technology[choice - 1])
