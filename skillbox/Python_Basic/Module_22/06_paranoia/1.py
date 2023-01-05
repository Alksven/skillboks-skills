def encryption():
    text = open('text.txt', 'r')
    a = text.read()
    print(a)
    ready_file = open('cipher_text.txt', 'a')
    for step, word in enumerate(a):
        for l in word:
            ready_file.write(letters[letters.index(l) + step + 1])
    ready_file.write('\n')




letters = 'abcdefghijklmnopqrstuvwxyz'




encryption()




