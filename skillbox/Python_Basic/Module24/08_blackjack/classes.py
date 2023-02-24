import random


class Card:

    def __init__(self, suit, value):
        self.card_suit = suit
        self.card_value = value


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
        self.deck = Deck()

    def add_cards(self):
        self.cards.append(self.deck.create())

    def info(self):
        self.summ_cards = [0]
        for i_card in self.cards:
            print(i_card.card_suit, i_card.card_value)
            if isinstance(i_card.card_value, int):
                self.summ_cards[0] += i_card.card_value
            elif i_card.card_value == 'T':
                self.summ_cards[0] += 11
            elif i_card.card_value in ['V', 'D', 'K']:
                self.summ_cards[0] += 10
            self.summ_cards.append(i_card.card_value)
            if self.summ_cards[0] > 21 and self.summ_cards.count('T') > 0:
                self.summ_cards[0] -= 10
        print('Количество очков:', self.summ_cards[0])
