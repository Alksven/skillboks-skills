class Square:

    def __init__(self, num: int) -> None:
        self.start = 0
        self.last = num + 1

    def __iter__(self):
        return self

    def __next__(self) -> int:
        self.start += 1
        if self.start == self.last:
            raise StopIteration
        print(self.start, end=' = ')
        return self.start ** 2


last_num = int(input('Введие число: '))

square = Square(num=last_num)

for i in square:
    print(i)