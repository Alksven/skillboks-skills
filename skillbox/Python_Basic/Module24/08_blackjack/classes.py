import random
class Card:
    pass
    #  Карта, у которой есть значения
    #   - масть
    #   - ранг/принадлежность 2, 3, 4, 5, 6, 7 и так далее


class Deck:

    def __init__(self):
        self.rang_deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'V', 'D', 'K', 'T']
        self.deck = {'♥': self.rang_deck.copy(), '♠': self.rang_deck.copy(), '♣': self.rang_deck.copy(),
                     '♦': self.rang_deck.copy()}

    def create(self):
        a = random.randint

class Player:
    pass
    #  Игрок, у которого есть имя и какие-то карты на руках
