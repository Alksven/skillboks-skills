import os

path_to = input('Enter the path:')

if os.path.isdir(path_to):
    print('this is a folder')
elif os.path.isfile(path_to):
    print('this is a file', os.path.getsize(path_to), 'byte')
else:
    print('no such path exists')
