text = input('Enter text')

new_list = [x for x in text if x.islower()]
print(new_list)