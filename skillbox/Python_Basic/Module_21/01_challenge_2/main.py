def numbers(stop, start=1, ):
    print(start)
    if start != stop:
        return numbers(stop, start + 1)


number = int(input('Введите num: '))
numbers(number)
