class SimpleIterable:
    def __getitem__(self, index):
        if 0 <= index <= 5:
            return index * 2
        else:
            raise IndexError


if __name__ == '__main__':
    iterable = SimpleIterable()
    for value in iterable:
        print(value)
    print('iterable[0] :', iterable[0])
    print('iterable[2] :', iterable[2])
    print('iterable[3] :', iterable[3])
    # print('iterable[-3] :', iterable[-3])

    iterator = iter(iterable)
    print('iterator = iter(iterable) :', iterator)
    print('next(iterator) :', next(iterator))
    print('next(iterator) :', next(iterator))
    print('next(iterator) :', next(iterator))
