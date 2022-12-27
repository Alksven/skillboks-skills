import os

rel_path = os.path.join('access', 'admin.bat')
abs_path = os.path.abspath(rel_path)
print('Absolute path to the file:', abs_path)
print('Relative path to the file:', rel_path)

