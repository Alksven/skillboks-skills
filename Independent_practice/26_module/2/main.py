class CountIterator:

    def __init__(self):
        self.count = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1
        return self.count - 1


my_iter = CountIterator()

for i_elem in my_iter:
    print(i_elem)