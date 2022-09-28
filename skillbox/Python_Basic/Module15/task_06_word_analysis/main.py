def get_input_parameters():

    enter_word = input('Введите слово: ')

    return enter_word


def display_result(number_unique_letters):

    print('Количество уникальных букв:', number_unique_letters)


def count_number_unique_letters(word):

    delete_list = []
    word_list = list(word)

    for i_letter_1 in range(len(word)):
        for i_letter_2 in range(i_letter_1 + 1, len((word))):
            if word_list[i_letter_1] == word_list[i_letter_2]:
                delete_list.append(word_list[i_letter_1])
                break

    for delete in delete_list:
        for clear in word_list:
            if delete == clear:
                word_list.remove(clear)

    answer = len(word_list)

    return answer


if __name__ == '__main__':

    word = get_input_parameters()
    number_unique_letters = count_number_unique_letters(word)
    display_result(number_unique_letters)
