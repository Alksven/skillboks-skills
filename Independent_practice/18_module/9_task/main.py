sentence = input('Enter text: ')

answer = [i for i in sentence if i.islower()]

if len(answer) > len(sentence) / 2:
    print(sentence.lower())
else:
    print(sentence.upper())