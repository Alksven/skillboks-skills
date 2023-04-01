from abc import ABC, abstractmethod


class Transport(ABC):
    def __init__(self, color: str, speed: int) -> None:
        self.color = color
        self.speed = speed

    def __str__(self):
        return f'{type(self).__name__} speed {self.speed}, color {self.color}'


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
amph_transport.sound()
amph_transport.ride_on_earth()
amph_transport.ride_on_water()
amph_transport.play_music()
print(amph_transport)
