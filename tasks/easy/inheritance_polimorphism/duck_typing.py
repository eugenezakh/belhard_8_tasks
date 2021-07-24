"""
Создать 3 класса:

Cat, Duck, Cow

в каждом классе определить метод says()

Cat.says() - кошка говорит мяу
Duck.says() - утка говорит кря
Cow.says() - корова говорит муу


Написать функцию animal_says(), которая принимает объект и вызывает метод says
"""


class Cat:

    @staticmethod
    def says(self):
        print("Кошка говорит мяу")


class Duck:

    @staticmethod
    def says(self):
        print("Утка говорит кря")


class Cow:

    @staticmethod
    def says(self):
        print("Корова говорит муу")


def animal_says(object_name):
    object_name.says()


a = Cat()
b = Cow()
c = Duck()
