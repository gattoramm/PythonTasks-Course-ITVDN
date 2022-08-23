class MyObject:
    def __init__(self):
        self.__attribute = 0
    
    @property
    def attribute(self):
        return self.__attribute

    @attribute.setter
    def attribute(self, value):
        self.__attribute = value

obj = MyObject()
print(obj.attribute)
obj.attribute = 20
print(obj.attribute)