# def fib_fun(num, fibonacci_list):
#     if len(fibonacci_list) + 1 == num:
#         return 0
#     else:
#         fibonacci_list.append(fibonacci_list[-2] + fibonacci_list[-1])
#         return fib_fun(num, fibonacci_list)
#
#
#
# num_fib =  6 #int(input('Введите позицию числа в ряде Фибоначчи: '))
# fibonacci_list = [0, 1]
#
# print('Число', fib_fun(num_fib, fibonacci_list))



def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))


