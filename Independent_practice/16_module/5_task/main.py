first_txt = input('Enter the first text: ')
second_txt = input('Enter the second text: ')

first_count = first_txt.count('!') + first_txt.count('?')
second_count = second_txt.count('!') + second_txt.count('?')

answer = 'Third message '

if first_count > second_count:
    answer += first_txt + ' ' + second_txt
    print(answer)

elif first_count < second_count:
    answer += second_txt + ' ' + first_txt
    print(answer)

else:
    print('WFT')