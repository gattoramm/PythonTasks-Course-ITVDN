class MyObject:
    def __init__(self):
        self.__private_attribute = 42
    
    def get_private(self):
        return self.__private_attribute

obj = MyObject()
print(obj.get_private())
#print(obj.__private_attribute)
print(obj._MyObject__private_attribute)