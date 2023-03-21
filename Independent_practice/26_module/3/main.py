import random


class SumsOfLastTwo:

    def __init__(self, count):
        self.last = 0
        self.start = 0
        self.end = count

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        if self.start > self.end:
            raise StopIteration
        self.last += random.random()
        return self.last


counter = SumsOfLastTwo(5)
for i in counter:
    print(round(i, 2))


