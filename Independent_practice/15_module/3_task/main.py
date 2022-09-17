count_dog = 6
dog_list = [6, 5, 7, 23, 45, 12, 9]
dog_lict_new = []
for i_count in range(count_dog):
    if dog_list[i_count] > dog_list[i_count + 1]:
        dog_lict_new.append(dog_list[i_count])
print(dog_lict_new)