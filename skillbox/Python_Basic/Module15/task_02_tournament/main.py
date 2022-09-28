def display_result(participants_names):

    print('Первый день:', participants_names)



def get_participants_names(names):

    name_list = []

    for index, name in enumerate(names):
        if index % 2 == 0:
            name_list.append(name)

    return name_list


if __name__ == '__main__':

    participants_names = get_participants_names(["Артемий", "Борис", "Влад", "Гоша", "Дима", "Евгений", "Женя", "Захар"])
    display_result(participants_names)
