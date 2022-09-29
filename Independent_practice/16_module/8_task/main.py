num_of_participants = int(input('Number of participants: '))
num_of_team_members = int(input('Number of team members: '))
participants_list = []
count = 1

if num_of_participants // num_of_team_members != 0:
    print('Error')

for _ in range(num_of_participants // num_of_team_members):
    participants_list.append(list(range(count, count + num_of_team_members)))
    count += num_of_team_members

print('General list of participants:', participants_list)
