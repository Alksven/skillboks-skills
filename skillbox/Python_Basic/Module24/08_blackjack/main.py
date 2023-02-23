from classes import Deck
from classes import Player
import random

deck = Deck()
p2 = Player('Вася')
p1 = []
print('Раздача:')
for i in range(2):
    p1.append(deck.create())
    p2.cards.append(deck.create())


# while len(deck.deck['♠'] + len(deck.deck['♥'] + len(deck.deck['♣'] + len(deck.deck['♦']) > 10:
