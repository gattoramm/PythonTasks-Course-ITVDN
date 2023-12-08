def sequence(values):
    print(values[1])
    print(values.__getitem__(1))


def print_slice():
    print(slice)
    print(slice(2, 5))
    print(slice(3, 6, None))


def slice_sequence(values):
    print(values[2:5])
    print(values[slice(2, 5)])
    print(values.__getitem__(slice(2, 5)))


if __name__ == "__main__":
    values = [5, 8, 2, 1, 9, 2]
    sequence(values)
    print()
    print_slice()
    print()
    slice_sequence(values)

