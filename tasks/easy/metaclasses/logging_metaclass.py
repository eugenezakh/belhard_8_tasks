"""
Описать логгирующий метакласс, который все методы класса будет логгировать, т.е.
до выполнения функции печатает на экран строку, вида
"Выполняем {func.__name__} с args: {args} и kwargs: {kwargs}".
После выполнения функции напечатать строку "Выполнено {func.__name__}"
"""
from types import FunctionType


def logging_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Выполняем {func} с args: {args} и kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Выполнено {func}")
        return result
    return wrapper


class LoggingMetaclass(type):
    def __new__(mcs, name, bases, attr):
        new_attribute = {}
        for attr_name, attr_value in attr.items():
            if isinstance(attr_value, FunctionType):
                attr_value = logging_decorator(attr_value)
            new_attribute[attr_name] = attr_value
        new_class = super().__new__(mcs, name, bases, new_attribute)
        return new_class


class TestClass(metaclass=LoggingMetaclass):
    name: str

    def __init__(self, name):
        self.name = name

    def say_name(self):
        print(f'{self.name}')


test = TestClass('Peter')
test.say_name()
