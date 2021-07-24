"""
Садовник, который может:
1. Ухаживать за растением
2. Собирать с него урожай

Атрибуты:
- **name** - имя садовника
- **plants** - список с растениями, за которыми ухаживает садовник

Методы:
- инициализатор init, который принимает name - имя садовника
  и args - произвольное количество кустов томата
- метод **work()**, который заставляет садовника работать, что позволяет всем растениям расти
- метод **harvest()**, который проверяет, все ли плоды созрели.
  Если созрели все плоды - садовник собирает урожай (метод возвращает список всех томатов),
  если нет - метод печатает предупреждение, что томаты не созрели и возвращает None.
"""


class Gardener:
    name: str
    plants: list

    def __init__(self, name, *args):
        self.name = name
        self.plants = list(args)

    def work(self):
        for i in self.plants:
            i.grow_all()

    def harvest(self):
        all_tomato = []
        for i in self.plants:
            if i.all_are_ripe() is False:
                break
            all_tomato.extend(i.tomato_list)
        else:
            return all_tomato
        print("Томаты пока не созрели.")
