student_info = input('Enter information about the student separated by a space'
                     ' (first name, last name, city, place of study, grades): ').split()

student_dict = dict()

student_dict['f_name'] = student_info[0]
student_dict['l_name'] = student_info[1]
student_dict['city'] = student_info[2]
student_dict['place_of_study'] = student_info[3]
student_dict['grades'] = []

for i_grades in student_info[4:]:
    student_dict['grades'].append(int(i_grades))


for i_info in student_dict:
    print(i_info, '-', student_dict[i_info])
