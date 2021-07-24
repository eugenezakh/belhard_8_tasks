"""
Создать класс Warrior

Определить атрибуты:

- name - имя юнита
- health_points - int от 0 до 100

Определить методы:

- инициализатор __init__, который создает юнита со 100 health_points
- метод hit, который реализует удар, от которого снимается 20 health_points
  у другого юнита

Создать список, в который добавить 5 объектов класса Warrior.

В случайном порядке они бьют друг друга. Тот, кто бьет, здоровья не теряет.
У того, кого бьют, оно уменьшается на 20 очков от одного удара.
После каждого удара надо выводить сообщение, какой юнит атаковал,
и сколько у противника осталось здоровья.
Как только у кого-то заканчивается ресурс здоровья он удаляется из списка.
Программа завершается, когда останется один юнит, на экран выводится сообщение о том,
кто одержал победу.
"""
import random


class Warrior:
    name: str
    health_points: int

    def __init__(self, name: str):
        self.name = name
        self.health_points = 100

    def __repr__(self):
        return f'{self.name}'

    def hit(self, other):
        other.health_points -= 20
        print(f'{self.name} атакует {other.name} и оставляет ему {other.health_points} здоровья')


class Battle:
    warriors: list

    def __init__(self, warriors):
        self.warriors = warriors

    def fight(self):
        while True:
            for i in range(len(self.warriors)):
                attack = random.choice(self.warriors)
                defence = random.choice(self.warriors)
                if attack.name == defence.name:
                    continue
                else:
                    Warrior.hit(attack, defence)
                if defence.health_points == 0:
                    print(f'{defence} погибает')
                    self.warriors.remove(defence)
                    print(f'Остались в живых вот эти ребята: {self.warriors}')
            if len(self.warriors) == 1:
                print(f'И победителем этой смачной зарубы становится {self.warriors}!')
                break


if __name__ == '__main__':
    war_1 = Warrior('Жанна Д\'Арк')
    war_2 = Warrior('Чак Норрис')
    war_3 = Warrior('Эдвард Руки-Ножницы')
    war_4 = Warrior('Дональд Трамп')
    war_5 = Warrior('Джереми Кларксон')

warriors = [war_1, war_2, war_3, war_4, war_5]
battle_1 = Battle(warriors)
battle_1.fight()
