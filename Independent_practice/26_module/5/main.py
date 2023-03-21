def gen(start):
    while True:
        yield start
        start += 1


b = gen(start=0)

for i in b:
    print(i)

