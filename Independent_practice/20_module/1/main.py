import random


def function(start, stop):
    list = [random.randint(start, stop) for _ in range(10)]
    return tuple(list)


first_tuple = function(0, 5)
second_tuple = function(-5, 0)
third_tuple = first_tuple + second_tuple

print(third_tuple)
print('number of 0:', third_tuple.count(0))
