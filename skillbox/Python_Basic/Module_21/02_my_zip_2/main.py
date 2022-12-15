def shortest(first, second):
    return min(len(first), len(second))


first = 'asfd'
second = [1, 2, 3, 4]

ready_list = [(first[i], second[i])
              for i in range(shortest(list(first), list(second)))]

print(ready_list)