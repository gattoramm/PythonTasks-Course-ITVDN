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


obj = D()
obj.method()
print(D.__mro__)
obj = E()
print(E.__mro__)

(A.method(C))
