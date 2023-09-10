"""
    Создайте класс, описывающий температуру и
    позволяющий задавать и получать температуру по шкале Цельсия и Фаренгейта, причём данные могут
    быть заданы в одной шкале, а получены в другой.
"""


class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273.13:
            raise ValueError("Temperature below -273.15 is not possible.")
        self._temperature = value


if __name__ == "__main__":
    celsius1 = Celsius(45)
    print(celsius1.temperature)
    print(celsius1.to_fahrenheit())
