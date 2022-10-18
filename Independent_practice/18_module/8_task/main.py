way = 'C:/user/docs/folder/new_file.txt'

drive = input('Emter drive ')
file = input('Enter File: ')

if not way.startswith(drive):
    print('Error.. Invalid drive.')
elif not way.endswith(file):
    print('Error.. Invalid file extension.')
else:
    print('The path is correct!')