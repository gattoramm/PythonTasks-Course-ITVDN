"""
    Аттрибуты класса, объекта
"""


class MyObject:
    int_field = 8
    str_field = "string"


if __name__ == "__main__":
    print("Методы аттрибуты класса MyObject:", dir(MyObject))
    print("Любой класс сам является значением-объектом: ", MyObject)
    print("Экземпляром класса type:", type(MyObject))
    print()
    print("Члены класса являются аттрибутами")
    print("Аттрибуты класса MyObject принадлежат самому классу:", MyObject.int_field, MyObject.str_field)

    AnotherClass = MyObject
    print("AnotherClass является:", AnotherClass)

    print()
    object1 = MyObject()
    object2 = MyObject()
    print("Через объекты класса тоже можем получить доступ к аттрибутам данного класса:",
          object1.int_field,
          object2.str_field)

    print()
    MyObject.int_field = 10
    print("Изменили аттрибут класса MyObject (MyObject.int_field = 10)")
    print("Аттрибут класса MyObject.int_field = ", MyObject.int_field)
    print("Аттрибут объекта object1.int_field = ", object1.int_field)

    print()
    object2.str_field = "new_string"
    print("Изменили аттрибут объекта object1 (object2.str_field = \"new_string\")")
    print("Аттрибут класса MyObject.str_field = ", MyObject.str_field)
    print("Аттрибут объекта object1.str_field = ", object1.str_field)
    print("Аттрибут объекта object2.str_field = ", object2.str_field)
