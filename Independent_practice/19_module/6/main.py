def function(text):
    text_dict = dict()
    for i in text:
        if i in text_dict:
            text_dict[i] += 1
        else:
            text_dict[i] = 1
    return text_dict


text = input('Enter text: ').lower()

answer = function(text)

for sym in sorted(answer.keys()):
    print(sym, ':', answer[sym])
print('Maximum frequency:', max(answer.values()))
