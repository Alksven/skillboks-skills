def sum(*args):
    resul = 0
    for listt in args:
        if isinstance(listt, int):
            resul += listt
        elif listt == []:
            return 0
        elif isinstance(listt, (list, tuple)):
            return sum(listt[0]) + sum(listt[1:])

    return resul




# print("Выпрямленный список: ", sum([[1, 2, [3]], [1], 3]))


