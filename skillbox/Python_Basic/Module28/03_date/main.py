class Date:
    """
    Класс, который устанавливает дату в формате dd-mm-yyyy и проверяет ее.
    """
    now_data: str = ''

    @classmethod
    def from_string(cls, data: str) -> str:
        """
        Метод, устанавливает дату и проверяет ее на корректность ввода
        :param data: Дата, которую хотим установить
        :return: Дату в формате День: dd  Месяц: mm  Год: yyyy
        :rtype: str
        """
        if '-' not in data or data.count('-') < 2:
            print('Неверный формат даты. Используйте "-" как разделитель')
        else:
            Date.now_data = data.split('-')
            return f'День: {Date.now_data[0]}  Месяц: {Date.now_data[1]}  Год: {Date.now_data[2]}'

    @classmethod
    def is_date_valid(cls, data: str) -> bool:
        """
        Метод, который проверяет, совпадает ли проверяемая дата с установленной
        :param data: Проверяемая дата
        :return: False либо True
        :rtype: bool
        """
        if data.split('-') != Date.now_data:
            return False
        return True



date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))