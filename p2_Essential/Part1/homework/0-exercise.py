"""
    Создайте класс, описывающий автомобиль. Создайте класс автосалона, содержащий в себе список
    автомобилей, доступных для продажи, и функцию продажи заданного автомобиля.
"""


class Automobile:
    def __init__(self, auto):
        self.auto = auto
    
    def __repr__(self):
        return "Automobile %s" % self.auto


class Automarket:
    def __init__(self, automarket):
        self.automarket = automarket
    
    def __repr__(self):
        return "Automarket %s" % self.automarket
    
    @classmethod
    def auto_in_salone(cls, auto):
        return cls(auto)


if __name__ == "__main__":
    auto1 = Automobile("BMW")
    auto2 = Automobile("Audi")
    auto3 = Automobile("Skoda")
    auto4 = Automobile("Ferrari")
    print(auto1)

    automarket1 = Automarket.auto_in_salone(auto1)
    automarket2 = Automarket.auto_in_salone(auto2)
    print(automarket1)
    print(automarket2)
