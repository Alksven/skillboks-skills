def get_input_parameters():
    shift = int(input('Сдвиг: '))
    sym_list = [1, 2, 3, 4, 5]
    return shift, sym_list


def display_result(shifted_list):
    print('Сдвинутый список:', shifted_list)



def shift_list(shift, original_list):
    new_list = original_list

    for count in range(shift):
        new_list = new_list[-1:]+new_list[:-1]

    return new_list


if __name__ == '__main__':

    shift, original_list = get_input_parameters()
    shifted_list = shift_list(shift, original_list)
    display_result(shifted_list)
