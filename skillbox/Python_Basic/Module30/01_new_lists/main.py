from functools import reduce

if __name__ == "__main__":
    floats: list[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
    names: list[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
    numbers: list[int] = [22, 33, 10, 6894, 11, 2, 1]

    floats_list = list(map(lambda x: round(x ** 3, 3), floats))
    print(floats_list)
    names_list = list(filter(lambda x: len(x) >= 5, names))
    print(names_list)
    numbers_list = reduce(lambda x, y: x * y, numbers)
    print(numbers_list)