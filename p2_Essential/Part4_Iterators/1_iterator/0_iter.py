def my_for(iterable, callback):
    it = iter(iterable)
    while True:
        try:
            value = next(it)
            callback(value)
        except StopIteration:
            break


def loop_body(value):
    print('Next value:', value)


if __name__ == "__main__":
    print('Пример iter()')
    values = [1, 2, 3, 5]
    it = iter(values)
    print('it = iter(values) :', it)
    print('next(it) :', next(it))
    print('next(it) :', next(it))
    print('next(it) :', next(it))
    print('next(it) :', next(it))

    my_for(values, loop_body)
