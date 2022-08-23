"""
    Создайте класс, описывающий автомобиль. Создайте класс автосалона, содержащий в себе список
    автомобилей, доступных для продажи, и функцию продажи заданного автомобиля.
"""


class Automobile:
    def __init__(self, auto):
        self.auto = auto
    
    def __repr__(self):
        return "Automobile %s" % self.auto


class Autosalone:
    def __init__(self, autosalone):
        self.autosalone = autosalone
    
    def __repr__(self):
        return "Autosalone %s" % self.autosalone
    
    @classmethod
    def auto_in_salone(cls, auto):
        return cls(auto)


if __name__ == "__main__":
    auto1 = Automobile("BMW")
    auto2 = Automobile("Audi")
    auto3 = Automobile("Skoda")
    auto4 = Automobile("Ferrari")
    print(auto1)

    autosalone1 = Autosalone.auto_in_salone(auto1)
    autosalone2 = Autosalone.auto_in_salone(auto2)
    print(autosalone1)
    print(autosalone2)
