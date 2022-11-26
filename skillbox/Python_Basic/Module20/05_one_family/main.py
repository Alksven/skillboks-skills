people = {
    ("Сидоров", "Никита"): 35,
    ("Сидорова", "Алина"): 34,
    ("Сидоров", "Павел"): 10,
    ("Иванов", "Коля"): 36,
    ("Иванова", "Алина"): 20,
    ("Иванова", "Галина"): 12,
}

surname = input('Введите фамилию: ').lower()

for i in people:
    if (surname.lower() == str(i[0].lower())) or (surname.lower() == str(i[0][0:-1].lower())) or (surname[0:-1].lower() == str(i[0].lower())):
        print(' '.join(i), people[i])

