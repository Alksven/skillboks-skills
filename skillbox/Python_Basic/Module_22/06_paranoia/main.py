def encryption():
    text = open('text.txt', 'r')
    ready_file = open('cipher_text.txt', 'a')

    for step, word in enumerate(text):
        for l in word:
            if l.isalpha():
                ready_file.write(length(step + 1, l))
            else:
                ready_file.write(l)
    text.close()
    ready_file.close()

def length(n_num, let):
    if let.isupper():
        letters = alphabet.upper()
    else:
        letters = alphabet.lower()
    if letters.index(let) + n_num >= len(letters):
        return letters[letters.index(let) + n_num - len(letters)]
    else:
        return letters[letters.index(let) + n_num]


alphabet = 'abcdefghijklmnopqrstuvwxyz'

encryption()
