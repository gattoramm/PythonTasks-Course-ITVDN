"""
    Статические методы и методы класса
"""


class MyObject:
    class_attribute = 8

    def __init__(self):
        self.data_attribute = 42

    def instance_method(self):
        print(self.data_attribute)
    
    @staticmethod
    def static_method():
        print(MyObject.class_attribute)


if __name__ == "__main__":
    print('Вызовем статический метод на классе - MyObject.static_method():')
    MyObject.static_method()
    obj = MyObject()
    print('Вызовем метод экземпляра класса - obj.instance_method():')
    obj.instance_method()
    print('Вызовем статический метод на экземпляре класса - obj.static_method():')
    obj.static_method()
