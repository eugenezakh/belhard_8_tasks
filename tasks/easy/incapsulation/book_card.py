"""
Создать класс BookCard, в классе должны быть закрытые атрибуты:

- author - автор
- title - название книги
- publishing_house - издательство
- year - год издания
- num_pages - количество страниц
- num_copies - тираж

Определить методы:

- инициализатор __init__
- магические методы сравнения для сортировки книг по году издания

в сеттерах сделать проверки на тип данных. Если тип данных не подходит, то генерировать
ValueError. Для года издания дополнительно проверить на валидность, num_pages и
num_copies должны быть больше 0

реализовать через property
"""


class BookCard:
    __author: str
    __title: str
    __publishing_house: str
    __year: int
    __num_pages: int
    __num_copies: int

    def __init__(self, author: str, title: str, publishing_house: str, year: int, num_pages: int, num_copies: int):
        self.__author = author
        self.__title = title
        self.__publishing_house = publishing_house
        self.__year = year
        self.__num_pages = num_pages
        self.__num_copies = num_copies

    def __eq__(self, other):
        return self.__year == other.__year

    def __lt__(self, other):
        return self.__year < other.__year

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, author):
        if type(author) != str:
            raise TypeError(f'Неверный тип данных {self.author}')
        else:
            self.__author = author

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        if type(title) != str:
            raise TypeError(f'Неверный тип данных {self.title}')
        else:
            self.__title = title

    @property
    def publishing_house(self):
        return self.__publishing_house

    @publishing_house.setter
    def publishing_house(self, publishing_house):
        if type(publishing_house) != str:
            raise TypeError(f'Неверный тип данных {self.publishing_house}')
        else:
            self.__publishing_house = publishing_house

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        if type(year) != int:
            raise TypeError(f'Неверный тип данных {self.year}')
        elif year <= 0:
            raise ValueError('Указанный год недействителен')
        else:
            self.__year = year

    @property
    def num_pages(self):
        return self.__num_pages

    @num_pages.setter
    def num_pages(self, num_pages):
        if type(num_pages) != int:
            raise TypeError(f'Неверный тип данных {self.num_pages}')
        elif num_pages <= 0:
            raise ValueError('Указан несуществующий номер страницы')
        else:
            self.__num_pages = num_pages

    @property
    def num_copies(self):
        return self.__num_copies

    @num_copies.setter
    def num_copies(self, num_copies):
        if type(num_copies) != int:
            raise TypeError(f'Неверный тип данных {self.num_copies}')
        elif num_copies <= 0:
            raise ValueError('Неверно задан тираж')
        else:
            self.__num_copies = num_copies
