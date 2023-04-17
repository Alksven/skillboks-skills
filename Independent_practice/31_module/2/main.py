import re

text = r'How much \wwood+?, would a \wwood+?chuck \dwwood+, chuck if a \wwood+?,chuck could chuck \wwood?,'

result_1 = re.findall(r'\\wwood\+\?,', text)

print(f'Список всех упоминаний шаблона: {result_1}')