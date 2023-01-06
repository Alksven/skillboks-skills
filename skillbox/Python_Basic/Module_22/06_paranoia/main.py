def encryption():

    text = open('text.txt', 'r')
    ready_file = open('cipher_text.txt', 'a')

    for step, word in enumerate(text):
        for l in word:
            if l.isalpha():
                if l.isupper():
                    ready_file.write(letters_upper[letters_upper.index(l) + step + 1])
                else:
                    ready_file.write(letters_lower[letters_lower.index(l) + step + 1])
            else:
                ready_file.write(l)

def length():




letters_lower = 'abcdefghijklmnopqrstuvwxyz'
letters_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'




encryption()
