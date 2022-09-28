def get_input_parameters():

    word = input('Введите слово: ')
    return word


def display_result(is_palindrome):

    if is_palindrome == True:
        print('Слово является палиндромом')
    else:
        print('Слово не является палиндромом')

def check_palindrome(word):
    word_list = list(word)
    new_word = ''

    for i_letter in range(len(word_list) - 1, -1, -1):
        new_word += word_list[i_letter]

    if word == new_word:
        return True
    else:
        return False

if __name__ == '__main__':

    word = get_input_parameters()
    is_palindrome = check_palindrome(word)
    display_result(is_palindrome)
