import zipfile

war = zipfile.ZipFile("voyna-i-mir.zip", "r")
file_list = war.namelist()

file = war.extractall()

text = open(file_list[0], 'r')
text_2 = text.read()
letters = set(text_2)
list_count = list()

for i in letters:
    if i.isalpha():
        list_count.append([text_2.count(i), i])

list_count.sort()

for i_2 in list_count:
    print(*i_2)

war.close()
text.close()