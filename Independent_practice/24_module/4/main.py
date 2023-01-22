class Family:
    family_name = 'Common family'
    money = 100000
    have_a_house = False

    def info_family(self):
        print('Family name:', self.family_name)
        print('Family funds:', self.money)
        print('Having a house:', self.have_a_house)
        print()

    def earn_money(self, add_money):
        self.money += add_money
        print('Earned {} money! Current value: {}'.format(
            add_money,
            self.money
        ))
        print()

    def buy_house(self, price_house, dis=0):
        if self.money >= price_house - (price_house / 100 * dis):
            self.have_a_house = True
        else:
            print('Not enough money!')
            print()



my_family = Family()
my_family.info_family()
print('Try to buy a house')
my_family.buy_house(10 ** 6)
if not my_family.have_a_house:
    my_family.earn_money(800000)
    print('Try to buy a house again')
    my_family.buy_house(10 ** 6, 10)

my_family.info_family()