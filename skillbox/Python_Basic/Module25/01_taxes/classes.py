class Property:

    def __init__(self, worth):
        self.worth = worth

    def tax_calculation(self):
        return self.worth / 1

    def __str__(self):
        return 'Tax for your {}'.format(self.__class__.__name__)


class Car(Property):

    def __init__(self, worth):
        super().__init__(worth)

    def tax_calculation(self):
        super().__str__()
        return round(self.worth / 200, 2)


class Apartment(Property):

    def __init__(self, worth):
        super().__init__(worth)

    def tax_calculation(self):
        super().__str__()
        return self.worth / 1000


class CountryHouse(Property):

    def __init__(self, worth):
        super().__init__(worth)

    def tax_calculation(self):
        super().__str__()
        return self.worth / 500