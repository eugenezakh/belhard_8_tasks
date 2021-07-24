"""
Описать класс Device. Реализовать метод process_doc, который будет генерировать
raise NotImplementedError

Описать класс Scanner, который наследуется от Device. Реализовать метод
process_doc, который будет печатать "Сканирую документ: {name}"

Описать класс Copier, который наследуется от Device. Реализовать метод
process_doc, который будет печатать "Делаю копию: {name}"

Описать класс MFU, который наследуется от Scanner и Copier
Реализовать метод process_doc, который будет печатать "Сканирую, отправляю факс: {name}"

Создать объект класса MFU. Потренироваться вызывать методы через super,
через имя класса. Просмотреть MRO
"""


class Device:
    document: str

    def __init__(self, document: str):
        self.document = document

    def process_doc(self):
        raise NotImplementedError('Не применимо')


class Scanner(Device):

    def process_doc(self):
        print(f'Сканирую документ {self.document}')


class Copier(Device):

    def process_doc(self):
        print(f'Делаю копию {self.document}')


class MFU(Scanner, Copier):

    def process_doc(self):
        print(f'Сканирую, отправляю на факс: {self.document}')


a = MFU('test')
a.process_doc()
