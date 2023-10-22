class A:
    def method(self):
        print("A")


class B(A):
    pass


class C(A):
    def method(self):
        print("C")


class D(B, C):
    pass


class E(C, B):
    pass


if __name__ == "__main__":
    obj = D()
    obj.method()
    print(D.__mro__)
    obj = E()
    print(E.mro())

    for cls in [A, B, C, D]:
        print(cls.__name__ + ":", cls.__mro__)

    (A.method(C))
