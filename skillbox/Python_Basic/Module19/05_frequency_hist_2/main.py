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
print('Оригинальный словарь частот:')
for sym in sorted(answer.keys()):
    print(sym, ':', answer[sym])

values_dict = dict()
time_list = []
for v in set(answer.values()):
    for k in answer:
        if answer[k] == v:
            time_list.append(k)
    values_dict[v] = time_list
    time_list = []

print('Инвертированный словарь частот:')
for k in values_dict:
    print(k, values_dict[k])