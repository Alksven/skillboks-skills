from classes import Deck
from classes import Player

def deal_cards():
    for i in range(2):
        computer.cards.append(deck.create())
        player.cards.append(deck.create())


deck = Deck()
computer = Player('Дилер')
player = Player('Вася')
while True:
    print('Раздача:')
    deal_cards()
    player.info()
    for _ in range(14):
        action = int(input('\n1 = Еще. 2 = Хватит\nВведите команду: '))
        if action == 1:
            player.cards.append(deck.create())
            player.info()
            continue
        if action == 2:
            print('Карты {}'.format(computer.name))
            computer.info()
            if player.summ_cards[0] > computer.summ_cards[0] and player.summ_cards[0] < 22:
                print('{} Победил\n'.format(player.name))
            elif player.summ_cards[0] == computer.summ_cards[0]:
                print('Ничья')
            else:
                print('{} Победил\n'.format(computer.name))

            next_tour = int(input('1 = Еще кон. 2 = Завершить игру.\nВведите команду: '))
            if next_tour == 2:
                print('Игра завершена')
                exit()
            if next_tour == 1:
                player.cards.clear()
                computer.cards.clear()
                break
