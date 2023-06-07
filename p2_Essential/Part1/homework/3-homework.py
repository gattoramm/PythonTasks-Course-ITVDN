"""
    Создайте класс, описывающий температуру и
    позволяющий задавать и получать температуру по шкале Цельсия и Фаренгейта, причём данные могут
    быть заданы в одной шкале, а получены в другой.
"""


class Temperature:
    def __init__(self):
        self.__temperature = 0

    @property
    def attribute(self):
        return self.__temperature
