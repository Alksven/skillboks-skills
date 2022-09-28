zoo = ['lion', 'kangaroo', 'elephant', 'monkey']
print('1 week', zoo)

new_animal = input('Enter new animal: ')
place = input('After whom? ')
i_animal = zoo.index(place)
zoo.insert(i_animal + 1, new_animal)

print('2 week', zoo)

delete_animal = input('Who mowed?: ')
zoo.remove(delete_animal)
print('3 week', zoo)