"""
Описать класс Shape - фигура, у которого должно быть 2 абстрактных метода:
- get_perimeter для расчета периметра
- get_square для расчета площади

Описать класс Circle для круга, отнаследоваться от фигуры
добавить недостающие атрибуты
перегрузить методы get_perimeter и get_square
Длина окружности = 2 * pi * r
Площадь = pi * r ** 2

Описать класс Rectangle для прямоугольника, отнаследоваться от фигуры
добавить недостающие атрибуты
перегрузить методы get_perimeter и get_square
Периметр = 2 * a + 2 * b
Площадь = a * b


Описать класс Square для квадрата, отнаследоваться от прямоугольника
перегрузить методы get_perimeter и get_square
Периметр = 4 * a
Площадь = a ** 2
"""

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):

    @abstractmethod
    def get_perimeter(self):
        pass

    @abstractmethod
    def get_square(self):
        pass


class Circle(Shape):
    radius: float

    def __init__(self, radius: float):
        self.radius = radius

    def get_perimeter(self):
        print(f'Длина окружности равна {2 * pi * self.radius}')

    def get_square(self):
        print(f'Площадь круга равна {pi * self.radius ** 2}')


class Rectangle(Shape):
    side_1: float
    side_2: float

    def __init__(self, side_1: float, side_2: float):
        self.side_1 = side_1
        self.side_2 = side_2

    def get_perimeter(self):
        print(f'Периметр прямоугольника равен {(self.side_1 + self.side_2) * 2}')

    def get_square(self):
        print(f'Площадь прямоугольника равна {self.side_1 * self.side_2}')


class Square(Rectangle):
    side_1: float

    def __init__(self, side_1: float):
        super().__init__(side_1, side_1)

    def get_perimeter(self):
        print(f'Периметр квадрата равен {self.side_1 * 4}')

    def get_square(self):
        print(f'Площадь квадрата равна {self.side_1 ** 2}')


a = Circle(6)
a.get_square()
a.get_perimeter()

b = Square(4)
b.get_square()
b.get_perimeter()

c = Rectangle(4, 5)
c.get_square()
c.get_perimeter()
