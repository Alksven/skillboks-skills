def numbers(stop, start=1, ):
    print(start)
    if start != stop:
        numbers(stop, start + 1)


number = int(input('Введите num: '))
numbers(number)
