"""
    Создайте класс, описывающий автомобиль. Создайте класс автосалона, содержащий в себе список
    автомобилей, доступных для продажи, и функцию продажи заданного автомобиля.
"""


class Automobile:
    def __init__(self, auto):
        self.auto = auto
    
    def __repr__(self):
        return "Automobile %s" % self.auto


class Shop:
    def __init__(self, shop):
        self.shop = shop
    
    def __repr__(self):
        return "Shop %s" % self.shop
    
    @classmethod
    def auto_in_shop(cls, auto):
        return cls(auto)


if __name__ == "__main__":
    auto1 = Automobile("BMW")
    auto2 = Automobile("Audi")
    auto3 = Automobile("Skoda")
    auto4 = Automobile("Ferrari")
    print(auto1)

    shop1 = Shop.auto_in_shop(auto1)
    shop2 = Shop.auto_in_shop(auto2)
    print(shop1)
    print(shop2)
