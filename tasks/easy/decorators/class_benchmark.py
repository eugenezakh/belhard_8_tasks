"""
Написать декоратор, который будет проводить бенчмарк всех методов класса.

До выполнения метода будет печатать:
Выполняем {func.__name__} с args: {args} и kwargs: {kwargs}
Время начала: {start_time}

После выполнения метода будет печатать:
Выполнено {func.__name__}
Время окончания: {end_time}
Всего затрачено времени на выполнение: {end_time - start_time}
"""
import time


def benchmark(func):
    def wrapper(*args, **kwargs):
        print(f"Выполняем {func.__name__} с args: {args} и kwargs: {kwargs}")
        start_time = time.time()
        print(f"Время начала: {start_time}")
        result = func(*args, **kwargs)
        print(f"Выполнено {func.__name__}")
        end_time = time.time()
        difference = end_time - start_time
        print(f"Время окончания: {end_time}")
        print(f"Всего затрачено времени на выполнение: {difference}")
        return result
    return wrapper


def class_benchmark(cls):
    call_attr = {k: v for k, v in cls.__dict__.items() if callable(v)}
    for name, val in call_attr.items():
        decorated = benchmark(val)
        setattr(cls, name, decorated)
    return cls


@class_benchmark
class Phone:
    brand: str
    model: str
    issue_year: int

    def __init__(self, brand, model, issue_year):
        self.brand = brand
        self.model = model
        self.issue_year = issue_year

    def __str__(self):
        return f'Бренд: {self.brand}\nМодель: {self.model}\nГод выпуска: {self.issue_year}'

    def receive_call(name: str):
        print(f'Звонит {name}')

    def get_info(self) -> tuple:
        new_tuple = (self.brand, self.model, self.issue_year)
        return new_tuple


test = Phone('Samsung', 'A31', 2020)
test.receive_call()
test.get_info()
