import re

text = 'How much wood would a woodchuck chuck if a woodchuck could chuck wood?'


result_1 = re.match(r'wo', text)
print(f'Определить, начинается ли текст с шаблона wo: {result_1}')

result_2 = re.search(r'wo', text)
print(f'Найти первое упоминание шаблона wo в тексте: {result_2}')
print(f'Содержимое найденной подстроки: {result_2.group()}')
print(f'Начальная позиция: {result_2.start()}')
print(f'Конечная позиция: {result_2.end()}')

result_3 = re.findall(r'wo', text)
print(f'Список всех упоминаний шаблона: {result_3}')

result_4 = re.sub(r'wo', 'ЗАМЕНА', text)
print(f'Текст после замены: {result_4}')


