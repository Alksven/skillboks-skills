text = input('Enter text: ')
text_unique = set(text)
number = '1234567890'

answer = [i for i in text_unique if i in number]

print(''.join(answer))