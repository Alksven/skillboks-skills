def function(first_list, second_list):
    ready_list = []

    if len(first_list) > len(second_list):
        for i in range(len(second_list)):
            ready_list.append((first_list[i], second_list[i]))

    elif len(first_list) < len(second_list):
        for i in range(len(first_list)):
            ready_list.append((first_list[i], second_list[i]))

    else:
        for i in range(len(second_list)):
            ready_list.append((first_list[i], second_list[i]))

    return ready_list


first = 'asdf'
second = (10, 20, 30, 40)

ready_list = function(list(first), list(second))

for i in ready_list:
    print(i)
