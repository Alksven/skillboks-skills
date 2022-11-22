def crypto(list):
    return [v for i, v in enumerate(list) if is_prime(i)]

def is_prime(i_num):
    if i_num < 2:
        return False
    count = 0
    for i in range(2, i_num // 2 + 1):
        if i_num % i == 0:
            count = count + 1
    if count <= 0:
        return True
    else:
        return False

print(crypto({0: 1, 2: 3, 4: 5, 6: 7, 8: 9}))



