class Toyota:

    def __init__(self, color, price, max_speed, current_speed=0):
        self.color = color
        self.price = price
        self.max_speed = max_speed
        self.current_speed = current_speed

    def info_a_car(self):
        print(self.color)
        print(self.price)
        print(self.max_speed)
        print(self.current_speed)

    def change_speed(self, new_speed):
        self.current_speed = new_speed


car_1 = Toyota('red', 1000000, 200)
car_1.change_speed(20)
car_1.info_a_car()
