import random
original_prices = [random.randint(-100, 100)]

new_prices = original_prices[:]

for i in range(len(original_prices)):

    if new_prices[i] < 0:

        new_prices[i] = 0

print("Мы потеряли: ",  sum(new_prices) - sum(original_prices))