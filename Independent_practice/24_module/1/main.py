import random

class Toyota:
    color = 'red'
    price = 1000000
    max_speed = 200
    speed_now = 0


car_third = Toyota()
car_third.speed_now = random.randint(0, 200)
print('Скорость первой тачки', car_third.speed_now)

car_third = Toyota()
car_third.speed_now = random.randint(0, 200)
print('Скорость второй тачки', car_third.speed_now)

car_third = Toyota()
car_third.speed_now = random.randint(0, 200)
print('Скорость третьей тачки', car_third.speed_now)