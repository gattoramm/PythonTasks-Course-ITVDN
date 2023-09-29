class Base:
    def method(self):
        print('Base')


class Child(Base):
    def child_method(self):
        print('child_method')

    def method(self):
        print('Child(Base)')


if __name__ == "__main__":
    obj = Child()
    obj.method()
    obj.child_method()
