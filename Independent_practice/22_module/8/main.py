import os
import random

file_num = open('numbers.txt', 'a')
answer = open('answer.txt', 'w')
summ = 0

for i in range(10):
    num = random.randint(0, 100)
    summ += num
    file_num.write(str(num)+'\n')

answer.write(str(summ))

file_num.close()
answer.close()


