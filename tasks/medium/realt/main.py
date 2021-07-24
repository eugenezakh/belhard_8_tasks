from house import House
from person import Person
from townhouse import TownHouse

if __name__ == '__main__':
    house_1 = House('Ангарская, 42', 55000, 63)
    house_2 = House('Дзержинского, 11', 93000, 58)
    house_3 = House('Есенина, 121', 71600, 58)
    house_4 = TownHouse('Ратомка, 12', 230000)
    house_5 = TownHouse('Раубичи, 11', 499000)
    person_1 = Person("Чак Норрис", 82)
    person_1.info()
    person_1.earn_money(53000)
    person_1.make_deal(house_1)
    person_1.earn_money(10000)
    person_1.make_deal(house_1)
