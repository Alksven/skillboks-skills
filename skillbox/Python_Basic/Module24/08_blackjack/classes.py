import random
class Card:

    def __init__(self, suit, value):
        self.card_suit = suit
        self.card_value = value

    #  Карта, у которой есть значения
    #   - масть
    #   - ранг/принадлежность 2, 3, 4, 5, 6, 7 и так далее


class Deck:

    def __init__(self):
        self.rang_deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'V', 'D', 'K', 'T']
        self.deck = {'♥': self.rang_deck.copy(), '♠': self.rang_deck.copy(), '♣': self.rang_deck.copy(),
                     '♦': self.rang_deck.copy()}

    def create(self):
        choice_card_suit = random.choice(list(self.deck.keys()))
        choice_card_value = random.choice(self.deck[choice_card_suit])
        self.deck[choice_card_suit].remove(choice_card_value)
        return Card(choice_card_suit, choice_card_value)




class Player:

    def __init__(self, name):
        self.name = name
        self.cards = list()
        self.dexk = Deck()


    def add_cards(self):
        self.cards.append(self.dexk.create())

    def info_print(self):
        print('У {} сейчас {} карт(ы):'.format(self.name, len(self.cards)))
        for i_card in self.cards:
            print(i_card.card_suit, i_card.card_value)


    #  Игрок, у которого есть имя и какие-то карты на руках
