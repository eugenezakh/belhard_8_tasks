"""
Описать класс Cars. Реализовать метод print_fuel_type, который будет генерировать
raise NotImplementedError

Описать класс PetrolMotorCars, который наследуется от Cars. Реализовать метод
print_fuel_type, который будет печатать "Бензин"

Описать класс ElectricMotorCars, который наследуется от Cars. Реализовать метод
print_fuel_type, который будет печатать "Электричество"

Описать класс HybridCars, который наследуется от PetrolMotorCars и ElectricMotorCars
Реализовать метод print_fuel_type, который будет печатать "Бензин + электричество"


Создать объект класса HybridCars. Потренироваться вызывать методы через super,
через имя класса. Просмотреть MRO
"""


class Cars:

    def print_fuel_type(self):
        raise NotImplementedError('Не применимо')


class PetrolMotorCars(Cars):
    def print_fuel_type(self):
        print("Бензин")


class ElectricMotorCars(Cars):
    def print_fuel_type(self):
        print("Электричество")


class HybridCars(PetrolMotorCars, ElectricMotorCars):
    def print_fuel_type(self):
        print("Бензин + электричество")


hybrid_car = HybridCars()
electro_car = ElectricMotorCars()
petrol_car = PetrolMotorCars()
hybrid_car.print_fuel_type()
electro_car.print_fuel_type()
petrol_car.print_fuel_type()
