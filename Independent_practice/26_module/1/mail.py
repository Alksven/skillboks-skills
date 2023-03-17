
def fun(iterator):
    print(iterator.__next__())

itimes = [10, 20, 30]

iterator = itimes.__iter__()

while True:
    try:
        fun(iterator)
    except StopIteration:
        print('Список закончился')
        break