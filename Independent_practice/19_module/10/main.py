import random
def min_num(num, num_nam):
    print(f'The minimum element of the {num_nam}st set: {min(num)}')
    num.remove(min(num))
    return num

def ad_number(num, nam_num):
    add_num = random.randint(100, 200)
    print(f'Random number for {nam_num}st set: {add_num}')
    num.add(add_num)
    return num




nums_1 = [29, 17, 10, 15, 13, 22, 12, 22, 7, 24, 26, 3, 11, 2, 3, 16, 19, 21, 2, 3, 8, 27, 2, 17, 2, 20, 12, 21, 3, 1]
nums_2 = [16, 21, 30, 24, 5, 7, 23, 13, 11, 5, 21, 5, 19, 9, 12, 9, 15, 16, 29, 8, 16, 1, 22, 15, 16, 9, 1, 13, 21, 21]

num_sorted_1 = set(nums_1)
num_sorted_2 = set(nums_2)

print('1st set:', num_sorted_1)
print('2st set:', num_sorted_2)
print()


min_num_1 = min_num(num_sorted_1, '1')
min_num_2 = min_num(num_sorted_2, '2')
print()

ad_num_1 = ad_number(min_num_1, '1')
ad_num_2 = ad_number(min_num_2, '2')
print()

union_list = ad_num_1.union(ad_num_2)

print('Union of sets:', union_list)
print('Intersection of many:', ad_num_1.intersection(ad_num_2))
print('Elements in nums_2 but not in nums_1:', ad_num_2.difference(ad_num_1))