class Base:
    def method(self):
        print('Base')


class Child(Base):
    def child_method(self):
        print('child_method')

    def method(self):
        print('Child(Base)')


obj = Child()
obj.method()
obj.child_method()