"""
Создать метакласс, который будет фиксировать тип атрибута с помощью аннотаций.
При попытке присвоить атрибуту объект не подходящего типа сгенерировать исключение
ValueError
"""


def attribute_checker(func):
    def wrapper(self, name, value):
        attribute_annotation = self.__annotations__.get(name)
        if type(value) != attribute_annotation and attribute_annotation is not None:
            raise ValueError('Вы что-то не то вводите')
        return func(self, name, value)
    return wrapper


class AttributeTypeMetaclass(type):

    def __new__(mcs, name, bases, attr):
        new_class = super().__new__(mcs, name, bases, attr)
        new_class.__setattr__ = attribute_checker(new_class.__setattr__)
        return new_class


class Strings(metaclass=AttributeTypeMetaclass):
    strings: str
    digits: int

    def __init__(self, strings, digits):
        self.strings = strings
        self.digits = digits

    def print_values(self, a):
        print(self.strings, a)


strings_1 = Strings('test', 1)
strings_2 = Strings('test_2', None)
print(strings_1.values)
print(strings_2.values)
