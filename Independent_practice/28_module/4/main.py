class File:
    def __init__(self, file_new, mode):
        self.file = open(file_new, mode)

    def __enter__(self):
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()





with File('example.txt', 'w') as file:
    file.write('Всем привет!')