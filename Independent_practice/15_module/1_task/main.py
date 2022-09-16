nums_list = []

n = int(input('Enter number of numbers: '))
for _ in range(n):
    num = int(input('Next number: '))
    nums_list.append(num)

maximum = nums_list[0]
minimum = nums_list[0]

for i in nums_list:
    if maximum < i:
        maximum = i
    if minimum > i:
        minimum = i

print('The maximum number in the list:', maximum)
print('The minimum number in the list:', minimum)