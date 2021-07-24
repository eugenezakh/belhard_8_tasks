"""
Человек может:
1. Предоставить информацию о себе
2. Заработать деньги
3. Купить дом

Атрибуты:
- **name** - имя
- **age** - возраст
- **money** - количество денег
- **realty** - недвижимость (список домов)

Методы:
- инициализатор init, который принимает name и age, присваивает их
  self.name и self.age соответственно. self.cash присваивает 0, а self.realty присваивает пустой список
- метод **info()**, который будет выводить поля name, age, realty и money.
- метод **earn_money()**, который принимает значение, на которое нужно увеличить money
- метод **make_deal()**, который принимает объект класса House или Townhouse,
  и если у человека достаточно денег, то списывает их с money и добавляет объект дома к self.realty
"""


class Person:
    name: str
    age: int
    money: float
    realty: list

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.money = 0
        self.realty = []

    def info(self):
        print(f'Имя: {self.name} '
              f'Возраст: {self.age} '
              f'Недвижимость в собственности: {self.realty} '
              f'Денег на счете: {self.money}.')

    def earn_money(self, increase: int):
        self.money += increase
        print(f'Заработали {increase}, теперь у нас {self.money}')

    def make_deal(self, house):
        if self.money >= house.cost:
            self.money -= house.cost
            self.realty.append(house)
            print(f'Продано! Вы стали владельцем {house}, осталось средств: {self.money}')
            return True
        else:
            print('У вас не хватает средств для покупки этой недвижимости. Пора на завод.')
            return False
