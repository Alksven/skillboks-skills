def factorial(number):
    if number == 1:
        return 1
    fact_n_1 = factorial((number - 1))
    return number * fact_n_1


number = int(input('What factorial do we want to know? '))
result = factorial(number)
print('Resul: ', result)
