
text = input('Enter text: ')
symbol = set(".,;:!?")
count = 0
for sym in text:
    if sym in symbol:
        count += 1
print('Number of punctuation marks:', count)
print(symbol)