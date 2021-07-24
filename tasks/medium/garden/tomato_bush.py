"""
Куст с помидорами может:
1. Расти вместе с томатами
2. Предоставлять информацию о зрелости всех томатов
3. Предоставлять урожай

Атрибуты:
- **tomato_list** - список всех томатов

Методы:
- инициализатор init, который принимает args - произвольное количество томатов
  и сохраняет их в self.tomato_list
- метод **grow_all()**, который будет переводить все объекты из списка томатов на следующий этап созревания
- метод **all_are_ripe()**, который будет возвращать True, если все томаты из списка стали спелыми, False, если нет
- метод **give_away_all()**, который будет возвращать список томатов и очищать его на кусте томатов после сбора урожая
"""

from tomato import Tomato


class TomatoBush:
    tomato_list: list = []

    def __init__(self, *args):
        self.tomato_list = list(args)

    def grow_all(self):
        for i in self.tomato_list:
            Tomato.grow(i)

    def all_are_ripe(self):
        for i in self.tomato_list:
            if Tomato.is_ripe(i):
                return True
            else:
                return False

    def give_away_all(self):
        tomato_list_ripe = [i for i in self.tomato_list]
        self.tomato_list.clear()
        return tomato_list_ripe
