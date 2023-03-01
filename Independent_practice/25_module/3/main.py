class Ship:

    def __init__(self, model):
        self.__model = model

    def __str__(self):
        return f"Model of the Ship: {self.__model}"

    def action(self):
        print('{} is sailing'.format(self.__model))


class Warship(Ship):

    def __init__(self, model, gun):
        super().__init__(model)
        self.gun = gun

    def attack(self):
        print('the Ship is attacking')



class CargoShip(Ship):

    def __init__(self, model):
        super().__init__(model)
        self.cargo = 0

    def loading(self, cargo):
        print('The ship was loaded with {} tons'.format(cargo))
        self.cargo += cargo
        print('Now the ship is loaded by {} tons'.format(self.cargo))

    def unloading(self, cargo):
        print('The ship was unloaded with {} tons'.format(cargo))
        self.cargo -= cargo
        print('Now the ship is loaded by {} tons'.format(self.cargo))


warship = Warship(model='war_5510', gun='Machine gun')
cargoShip = CargoShip(model='cargo_5632')
print(warship)
print(cargoShip)
warship.action()
cargoShip.action()
warship.attack()
cargoShip.loading(cargo=10)
cargoShip.unloading(cargo=5)