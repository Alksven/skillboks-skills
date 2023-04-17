import re

text = 'Even if they are djinns, I will get djinns that can outdjinn them.'

result_1 = re.findall(r"\b[aAeEiIoOuUyY]\w*", text)
print(result_1)
result_2 = re.findall(r"\b[^aAeEiIoOuUyY\W]\w*", text)
print(result_2)