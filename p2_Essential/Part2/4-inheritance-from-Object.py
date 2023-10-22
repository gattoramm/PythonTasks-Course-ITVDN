class MyObject(object):
    pass


class MyObject1:
    pass


if __name__ == "__main__":
    print(type(MyObject))
    print(type(MyObject1))

    print(MyObject1.__bases__)
