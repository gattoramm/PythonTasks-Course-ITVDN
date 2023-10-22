class Base:
    def method(self):
        print('Base method invoked on', type(self).__name__, 'instance')


class Child(Base):
    def method(self):
        super().method()
        print('Child method invoked on', type(self).__name__, 'instance')


if __name__ == "__main__":
    base_instance = Base()
    base_instance.method()
    print()

    child_instance = Child()
    child_instance.method()
    print()

    #Base.method(child_instance)
