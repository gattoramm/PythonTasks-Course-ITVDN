"""
    Отношение между функцией класса и функцией экземпляра класса.
    Привязанный метод.
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print(self.name, "is", self.age)


if __name__ == "__main__":
    john = Person("John", 22)
    lucy = Person("Lucy", 21)

    print("Вызовем метод print_info как функцию внутри класса Person как его аттрибут:")
    Person.print_info(john)
    Person.print_info(lucy)

    print()
    print("Вызовем метод print_info как функцию конкретного объекта:")
    john.print_info()
    lucy.print_info()

    print()
    print("Person.print_info :", Person.print_info)
    print("john.print_info :", john.print_info)
    print("john.print_info вызывает Person.print_info(john)")
