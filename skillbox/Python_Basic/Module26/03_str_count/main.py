import os


def gen_files_path(directory):
    for i in os.listdir(directory):
        path = os.path.join(directory, i)
        if os.path.isfile(path) and path.endswith('.py'):
            yield count_str(path)


def count_str(path):
    count_in_file = 0
    with open(path, 'r') as file_is_open:
        for str_code in file_is_open:
            if str_code == '\n' or str_code.startswith('#'):
                continue
            else:
                count_in_file += 1
        return count_in_file


root_directory = '/home/ven/123'
file_search = gen_files_path(root_directory)

summ_str = 0

for i in file_search:
    summ_str += i

print(summ_str)
