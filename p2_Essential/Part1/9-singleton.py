class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = object.__new__(cls)

        return cls._instance

    def __init__(self):
        self.value = "some value"


if __name__ == "__main__":
    print(Singleton._instance)
    obj1 = Singleton()
    print(obj1)
    obj2 = Singleton()
    print(obj2)
