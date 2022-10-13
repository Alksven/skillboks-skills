import random

team_1 = [round(random.uniform(5.00, 10.00), 2) for _ in range(10)]
team_2 = [round(random.uniform(5.00, 10.00), 2) for _ in range(10)]
win_team = [team_1[i] if team_1[i] > team_2[i] else team_2[i] for i in range(10)]

print(f'Первая команда: {team_1} \nВторая команда: {team_2} \nПобедители тура: {win_team}')
