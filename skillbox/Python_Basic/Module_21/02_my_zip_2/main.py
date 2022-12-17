def zipp(*args):
    length = min(len(element) for element in args)
    new_list = [[item for index, item in enumerate(element) if index < length]for element in args]
    list_two = [[new_list[second_index][first_index] for second_index in range(len(new_list))]
                for first_index in range(length)]
    tuple_list = [tuple(list_two[index]) for index in range(length)]
    print(tuple_list)


a = [1, 2, 3, 4, 5]

b = {1: "s", 2: "q", 3: 4}

x = (1, 2, 3, 4, 5)

zipp(a, b, x)