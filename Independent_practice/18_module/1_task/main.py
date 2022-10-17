import random

name = input('Name: ')
order = random.randint(1, 10000)

message = 'Hello, {name}! Your number order: {order}. Have a good day!'.format(
    name=name,
    order=order
)
print(message)