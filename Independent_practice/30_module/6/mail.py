from functools import reduce


def my_add(sen_1, sen_2):
    if type(sen_1) != int:
        result = sen_1.split().count('was') + sen_2.split().count('was')
    else:
        result = sen_1 + sen_2.split().count('was')
    return result


sentences = ["Nory was a Catholic", "because her mother was a Catholic", "and Nory’s mother was a Catholic", "because her father was a Catholic", "and her father was a Catholic", "because his mother was a Catholic", "or had been"]


print(reduce(my_add, sentences))

