class MyObject:
    def __init__(self):
        self.password = None

    def __getattribute__(self, item):
        if item == 'secret_field' and self.password == "97686576":
            return "Secret value"
        else:
            return object.__getattribute__(self, item)


if __name__ == "__main__":
    obj = MyObject()
    print(obj.password)
    # print(obj.secret_field) #error
    obj.password = "97686576"
    print(obj.secret_field)
