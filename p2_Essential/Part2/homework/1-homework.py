"""
    Создайте иерархию классов транспортных средств. В общем классе опишите общие для всех транспортных средств поля, в
    наследниках – специфичные для них. Создайте несколько экземпляров. Выведите информацию о каждом транспортном
    средстве.
"""


class Transport:
    name = 'Transport'
    speed = 0


class Automobile(Transport):
    sub_name = 'Automobile'
    speed = 100


class Airplane(Transport):
    sub_name = 'Airplane'
    speed = 1000


if __name__ == "__main__":
    transport = Transport()
    print(transport.name)

    car = Automobile()
    print(car.name)
    print(car.sub_name)
    print(car.speed)

    airplane = Airplane()
    print(airplane.name)
    print(airplane.sub_name)
    print(airplane.speed)
