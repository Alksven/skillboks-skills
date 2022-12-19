nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]

def flatten(list_num):
    if list_num == []:
        return list_num
    if isinstance(list_num[0], list):
        return(flatten(list_num[0]) + flatten(list_num[1:]))
    return(list_num[:1] + flatten(list_num[1:]))

print("Выпрямленный список: ", flatten(nice_list))
