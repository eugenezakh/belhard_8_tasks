"""
Предположим, нас утомило задание атрибутов в конструкторе init(self, *args,
**kwargs). Хотелось бы ускорить этот процесс таким образом, чтобы была
возможность задавать атрибуты прямо при создании объекта класса.

class Man(object):
    pass

me = Man(height = 180, weight = 80)
Traceback (most recent call last):
File "<stdin>", line 20, in <module>
    TypeError: object.new() takes no parameters

Сделать возможным данный механизм
"""


class InitAttr(type):

    def __new__(mcs, name, bases, attrs):
        return super().__new__(mcs, name, bases, attrs)

    def __call__(self, *args, **kwargs):
        new_object = super().__call__(*args)
        for key in kwargs:
            setattr(new_object, key, kwargs[key])
        return new_object


class Man(metaclass=InitAttr):
    pass


me = Man(height=180, weight=80)
print(me.height)
print(me.weight)
