students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


pairs = []
hobby = []
surname = ''

for i in students:
    pairs.append(tuple((i, students[i]['age'])))
    hobby += (students[i]['interests'])
    hobby = tuple(hobby)
    surname += students[i]['surname']

print('Список пар "ID студента — возраст":', pairs)
print('Полный список интересов всех студентов:', hobby)
print('Общая длина всех фамилий студентов:', len(surname))