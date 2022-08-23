class MyObject:
    def __init__(self):
        self.__private_attribute = 42
    
    def get_private(self):
        return self.__private_attribute

    def set_attribute(self, value):
        self.__private_attribute = value

obj = MyObject()
print(obj.get_private())
obj.set_attribute(100)
print(obj.get_private())