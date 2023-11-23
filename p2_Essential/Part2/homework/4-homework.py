"""
    Создайте иерархию классов с использованием множественного наследования. Выведите на экран порядок разрешения методов
    для каждого из классов. Объясните, почему линеаризации данных классов выглядят именно так.
"""


class A:
    def method(self):
        print("A")


class B(A):
    pass


class C(A):
    def method(self):
        print("C")


class D(A):
    def method(self):
        print("D")


class EBC(B, C):
    pass


class ECB(C, B):
    pass


class EDB(D, B):
    pass


class EBD(B, D):
    pass


class EDC(D, C):
    pass


class ECD(C, D):
    pass


if __name__ == "__main__":
    objEBC = EBC()
    objEBC.method()
    print(EBC.__mro__)

    print(ECB.mro())
    print(EDB.mro())
    print(EBD.mro())
