class Countainer:
    """Class Container"""
    attr = 'value'


if __name__ == '__main__':
    for i in Countainer.__dict__:
        print(i, ' :', Countainer.__dict__[i])

    print(type(Countainer.__dict__))
