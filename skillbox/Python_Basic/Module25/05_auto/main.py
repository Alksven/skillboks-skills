from classes import Car

x = float(input('Enter X: '))
y = float(input('Enter Y: '))
a = int(input('Enter Angle: '))

car = Car(x=x, y=y, a=a)
while True:
    car.forward_movement()
    f = int(input())

# Enter
# X: 10
# Enter
# Y: 1
# Enter
# Angle: 225
# На
# какое
# расстояние
# проехала
# машина?11
# new
# X: 2.2
# new
# Y - 6.8