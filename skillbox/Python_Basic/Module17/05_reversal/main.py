word = input('Введите строку: ')

answer_list = [i for i in range(len(word)) if word[i] == 'h']

print('Развёрнутая последовательность между первым и последним h:',
      word[answer_list[-1] - 1:answer_list[0]:-1])
