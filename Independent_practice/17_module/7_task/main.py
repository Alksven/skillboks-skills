import random
original_prices = [random.randint(-100, 100) for x in range(10)]

new_prices = original_prices[:]

for i in range(len(original_prices)):

    if new_prices[i] < 0:

        new_prices[i] = 0

print("Мы потеряли: ", sum(original_prices) - sum(new_prices))
print(original_prices)
print(new_prices)
