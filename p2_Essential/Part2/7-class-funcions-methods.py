class MethodContainer:
    def __init__(self, data):
        self.data = data
    
    def method(self):
        print("method invoke")
        print("data = ", self.data)


if __name__ == "__main__":
    instance = MethodContainer(8)
    print("MethodContainer.method:", type(MethodContainer.method))
    print("instance.method:", type(instance.method))
    print()

    MethodContainer.method(instance)    # Вызов метода как функцию класса
    print()
    instance.method()   # Вызов метода
    print()

    print(MethodContainer.method.im_func)
    print(MethodContainer.method.im_func)
    print(instance.method)
