text = open('zen.txt', 'r')

del_sym = [i.strip() for i in text]
ready_text = del_sym[::-1]

for i in ready_text:
    print(i)

text.close()