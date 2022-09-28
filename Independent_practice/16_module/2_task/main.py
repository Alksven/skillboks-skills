employees = int(input('How many total employees? '))
salary_list = []

for count in range(employees):
    print(f'Salary of {count + 1} employee:', end=' ')
    salary = int(input())
    salary_list.append(salary)


for i_salary, num_salary in enumerate(salary_list):
    if num_salary == 0:
        salary_list.remove(salary_list[i_salary])

print(f'Remaining employees: {len(salary_list)} \nSalaries:{salary_list}')
print('Minimum:', min(salary_list), 'Maximum:', max(salary_list))