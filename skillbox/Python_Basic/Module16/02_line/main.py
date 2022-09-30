school_list_1 = []
school_list_2 = []

school_list_1.extend(list(range(160, 176 + 1, 2)))
school_list_2.extend(list(range(162, 180 + 1, 3)))

school_list_1.extend(school_list_2)

print('Отсортированный список учеников: ', sorted(school_list_1))
