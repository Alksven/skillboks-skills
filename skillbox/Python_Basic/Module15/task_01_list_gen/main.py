def get_input_parameters():

    number = int(input('Введите положитлеьное число '))
    return number



def display_result(odd_numbers):

    print(odd_numbers)



def get_odd_numbers(number):

    number_list = []

    for count in range(number + 1):
        if count % 2 != 0:
            number_list.append(count)

    return number_list



if __name__ == '__main__':

    number = get_input_parameters()
    odd_numbers = get_odd_numbers(number)
    display_result(odd_numbers)
