import random

squad_1 = [random.randint(50, 80)for _ in range(10)]
squad_2 = [random.randint(30, 60)for _ in range(10)]
squad_3_condition = ['KILL'if squad_1[fire] + squad_2[fire] > 100 else 'LIVE' for fire in range(10)]

print(squad_3_condition)