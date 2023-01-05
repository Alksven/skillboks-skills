import os

letters = ['abcdefghijklmnopqrstuvwxyz']
text = open('text.txt', 'r')

for n_str, word in enumerate(text):
    for i in word:
        print(letters[i])







