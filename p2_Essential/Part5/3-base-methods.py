def _in(item, values):
    print(item in values)
    print(item not in values)
    print(values.__contains__(item))


def _plus(item1, item2):
    print(item1 + item2)


def _mul(item1, val):
    print(item1 * val)


def _count(values, item):
    print(values.count(item))


if __name__ == "__main__":
    print("\t\t\tin")
    _in(2, [1, 2, 5])
    _in(3, [1, 2, 5])
    _in('h', 'hello')
    _in('lo', 'hello')
    print("\t\t\tplus")
    _plus("hello", "world")
    _plus([1, 2, 5], [7, 8])
    print("\t\t\tmultiply")
    _mul(3, [1, 0])
    _mul(50, "*")
    print("\t\t\tindex")
    print([5, 1, 2, 8, 2].index(2))
    print([5, 1, 2, 8, 2].index(2, 3))
    print([5, 1, 2, 8, 2].index(8, 1, 5))
    print('asdasdfdsase'.index('s'))
    print('asdasdfdsase'.index('das'))
    print("\t\t\tcount")
    _count([5, 1, 2, 8, 2], 2)
    _count([5, 1, 2, 8, 2], 8)
    _count([5, 1, 2, 8, 2], 17)
    _count('asdasdfdsase', 's')
    _count('asdasdfdsase', 'as')
