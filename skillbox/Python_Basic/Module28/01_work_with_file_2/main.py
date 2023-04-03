from typing import IO
class File:
    """
    Класс, который принимает пусть к файлу и открывает его в режиме чтения, Если файла нет, создает его.
    Args:
        path (str): путь к файлу

    """
    def __init__(self, path: str) -> None:
        self.path = path
        self.mode = 'r'

    def __enter__(self) -> IO:
        """
        Метод который либо открывает существующий файл либо создает его.
        :return: файл готовый для записи либо для чтения.
        """
        try:
            self.file = open(self.path, self.mode)
            return self.file
        except FileNotFoundError:
            self.file = open(self.path, 'a')
            return self.file

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        """
        Метод обрабатывающий исключения и закрывающий файл
        :param exc_type: Тип исключения.
        :param exc_val: Экземпляр исключения.
        :param exc_tb: Объект traceback.
        :return: bool
        """
        self.file.close()
        return True



with File('example.txt') as new_file:
    pass

