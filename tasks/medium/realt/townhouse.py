"""
Типовой дом

Методы:
- инициализатор init, который принимает адрес и начальную стоимость дома.
  self.area по умолчанию присваиваем 60
"""
from house import House


class TownHouse(House):
    def __init__(self, address, cost):
        super().__init__(address, 60, cost)
