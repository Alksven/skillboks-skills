class MyMath:
    """
    Класс, который выполняет матетические вычисления:
    - вычисление длины окружности.
    - вычисление площади окружности.
    - вычисление объёма куба.
    - вычисление площади поверхности сферы.
    Attributes:
        PI (int): Число PI
    """
    PI = 3.14

    @classmethod
    def circle_len(cls, radius: float) -> float:
        """
        Метод вычисляет длину окружности.
        :param radius: Радиус
        :return: Длина окружности
        :rtype: float
        """
        return 2 * MyMath.PI * radius

    @classmethod
    def circle_sq(cls, radius: float) -> float:
        """
        Метод вычисляет площадь окружности.
        :param radius: Радиус
        :return: Площадь окружности
        :rtype: float
        """
        return MyMath.PI * radius ** 2

    @classmethod
    def cube_volume(cls, height_cube: float) -> float:
        """
        Метод вычисляет объём куба.
        :param height_cube: Высота ребра куба
        :return: Объём куба
        :rtype: float
        """
        return height_cube ** 3

    @classmethod
    def sphere_surface(cls) -> float:
        """
        Метод вычисляет площадь поверхности сферы через радиус и диаметр.
        :return: Площадь
        :rtype: float
        """
        data: int = int(input('Вычисляем через радиус(1) или диаметр(2)'))
        if data == 1:
            radius: int = int(input('Введите радиус: '))
            return 4 * MyMath.PI * radius ** 2
        else:
            d: int = int(input('Введите диаметр: '))
            return 4 * MyMath.PI * (d/2) ** 2