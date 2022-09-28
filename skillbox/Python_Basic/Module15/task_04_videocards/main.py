def get_input_parameters():

    all_cards = int(input('Количество видеокарт: '))
    card_list = []

    for count_card in range(all_cards):
        print(f'{count_card + 1} Видеокарта:', end=' ')
        card = int(input())
        card_list.append(card)

    return card_list


def display_result(old_video_cards, new_video_cards):

    print('Старый список видеокарт:', old_video_cards)
    print('Новый список видеокарт:', new_video_cards)


def select_video_cards(video_cards):

    video_cards_sorted = sorted(video_cards)
    new_list_cards = []

    for i_cards in video_cards:
        if i_cards == video_cards_sorted[-1]:
            continue
        new_list_cards.append(i_cards)

    return new_list_cards


if __name__ == '__main__':

    video_cards = get_input_parameters()
    result_video_cards = select_video_cards(video_cards)
    display_result(video_cards, result_video_cards)
