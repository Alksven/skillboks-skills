words = input('Enter words separated by spaces: ').split()
text = input('Enter Text: ').split()

answer_list = [[i, text.count(i)] for i in words]
print(' '.join(str(answer_list)))