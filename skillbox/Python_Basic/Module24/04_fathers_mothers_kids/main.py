from classes import Parent
from classes import Child
import random

number_of_parents = int(input('Number of parents? '))
for _ in range(number_of_parents):
    name_parent, age_parent = input("Enter parent's name and age: ").split()
    Parent(name_parent, age_parent)

    have_many_children = int(input('How many children does {} have? '.format(name_parent)).lower())
    if have_many_children > 0:
        for _ in range(have_many_children):
            name_child, age_child = input("Enter child's name and age: ").split()
            Child(name_child, age_child)
            if Parent.parents_list[-1].age - int(age_child) > 16:
                Parent.parents_list[-1].children_list.append(Child.children[-1])
            else:
                print("the age difference is too small.")
                continue

