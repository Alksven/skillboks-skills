from abc import ABC, abstractmethod


class Transport(ABC):
    def __init__(self, color: str, speed: int) -> None:
        self._color = color
        self._speed = speed

    def __str__(self):
        return f'{type(self).__name__} speed {self._speed}, color {self._color}'

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, new_color):
        self._color = new_color

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, new_speed):
        self._speed = new_speed


    def sound(self):
        print(f'Сигнал')

    @abstractmethod
    def ride_on_earth(self):
        pass

    @abstractmethod
    def ride_on_water(self):
        pass


class MusicMixin:

    def play_music(self):
        print("""
        I see trees of green
        Red roses too
        I see them bloom
        For me and for you
        And I think to myself
        What a wonderful world
        """)

class Car(Transport):

    def ride_on_earth(self):
        print("Едем по земле")


class Boal(Transport):

    def ride_on_water(self):
        print("Ходим по воде")


class Amphibian(Boal, Car, MusicMixin):
    pass


amph_transport = Amphibian(color='red', speed=40)
print(amph_transport)
print(amph_transport.color, amph_transport.speed)
amph_transport.color = 'green'
amph_transport.speed = 500
print(amph_transport)
