def get_input_parameters():
    containers = int(input('Кол-во контейнеров: '))
    container_list = []

    for _ in range(containers):
        add_container = int(input('Введите вес контейнера:'))
        if add_container > 200:
            print('Слишком большой вес')
            continue
        container_list.append(add_container)

    new_container = int(input('Введите вес нового контейнера:'))

    return container_list, new_container


def display_result(serial_number_new_container):

    print('Номер, который получит новый контейнер:', serial_number_new_container)


def search_serial_number_new_container(list_container_weights, new_container_weight):

    sorted_list_container_weights = sorted(list_container_weights)
    place = 0
    answer = len(list_container_weights)

    for i_container, w_container in enumerate(sorted_list_container_weights):
        while new_container_weight > w_container:
            place = i_container
            break
    answer -= place

    return answer


if __name__ == '__main__':

    list_container_weights, new_container_weight = get_input_parameters()
    serial_number_new_container = search_serial_number_new_container(list_container_weights, new_container_weight)
    display_result(serial_number_new_container)
