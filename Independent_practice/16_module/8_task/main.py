num_of_part = int(input('Number of participants: '))
num_of_t_mem = int(input('Number of team members: '))
participants_list = []
count = 1

if num_of_part // num_of_t_mem != 0:
    print('Error')

for _ in range(num_of_part // num_of_t_mem):
    participants_list.append(list(range(count, count + num_of_t_mem)))
    count += num_of_t_mem

print('General list of participants:', participants_list)
