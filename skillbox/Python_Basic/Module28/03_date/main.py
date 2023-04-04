class Date:
    """
    Класс, который устанавливает дату в формате dd-mm-yyyy и проверяет ее.
    """
    def __init__(self, dd: int, mm: int, yyyy: int) -> None:
        self.dd = dd
        self.mm = mm
        self.yyyy = yyyy

    def __str__(self):
        return f'День: {self.dd}  Месяц: {self.mm}  Год: {self.yyyy}'

    @classmethod
    def from_string(cls, data: str) -> 'Date':
        """
        Метод, устанавливает дату и проверяет ее на корректность ввода
        :param data: Дата, которую хотим установить
        :return: Объект класса Date
        :rtype: Date
        """
        if '-' not in data or data.count('-') < 2:
            print('Неверный формат даты. Используйте "-" как разделитель')
        dd, mm, yyyy = map(int, data.split('-'))
        data_obj = cls(dd, mm, yyyy)
        return data_obj

    @classmethod
    def is_date_valid(cls, data: str) -> bool:
        """
        Метод, который проверяет, совпадает ли проверяемая дата с установленной
        :param data: Проверяемая дата
        :return: False либо True
        :rtype: bool
        """
        dd, mm, yyyy = map(int, data.split('-'))
        return 1 <= dd <= 31 and 1 <= mm <= 12 and yyyy < 9999


date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('3-13-2077'))