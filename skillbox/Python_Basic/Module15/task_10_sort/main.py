def get_input_parameters():
    numbers_list = [1, 4, -3, 0, 10]
    return numbers_list


def display_result(sorted_list):
    print(sorted_list)


def sort_list(original_list):
    numbers_list = sorted(original_list)
    return numbers_list


if __name__ == '__main__':

    original_list = get_input_parameters()
    sorted_list = sort_list(original_list)
    display_result(sorted_list)
