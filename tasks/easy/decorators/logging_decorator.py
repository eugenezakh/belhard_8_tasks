"""
Написать логгирующий декоратор, который все методы класса будет логгировать, т.е.
до выполнения функции печатает на экран строку, вида
"Выполняем {func.__name__} с args: {args} и kwargs: {kwargs}".
После выполнения функции напечатать строку "Выполнено {func.__name__}"
"""


def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Выполняем {func.__name__} с args: {args} и kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Выполнено {func.__name__}")
        return result
    return wrapper


def class_decorator(cls):
    call_attr = {k: v for k, v in cls.__dict__.items() if callable(v)}
    for name, val in call_attr.items():
        decorated = log_decorator(val)
        setattr(cls, name, decorated)
    return cls


@class_decorator
class SomeClass:
    def __init__(self):
        pass

    def some_function(self):
        print("some text")


a = SomeClass()
a.some_function()
