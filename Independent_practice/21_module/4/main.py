import random


def change_dict(dct):
    num = random.randint(1, 100)
    for i_key, i_value in dct.items():
        if isinstance(i_value, list):
            i_value.append(num)
        if isinstance(i_value, dict):
            i_value[num] = i_key
        if isinstance(i_value, set):
            i_value.add(num)


nums_list = [1, 2, 3]
some_dict = {1: 'text', 2: 'another text'}
uniq_nums = {1, 2, 3}
# Решить это задание можно разными способами
# Мы можем вручную копировать каждый входящий элемент:
common_dict = {1: nums_list.copy(), 2: some_dict.copy(), 3: uniq_nums.copy(), 4: (10, 20, 30)}
change_dict(common_dict)
print(common_dict)
# Либо мы можем применить вспомогательную функцию, которая сделает это за нас:
import copy

common_dict = {1: nums_list, 2: some_dict, 3: uniq_nums, 4: (10, 20, 30)}
common_dict_2 = copy.deepcopy(common_dict)  # Она будет особенно полезна в структурах, в которых множество вложенных переменных
change_dict(common_dict_2)
print(common_dict_2)

print(nums_list, some_dict, uniq_nums)