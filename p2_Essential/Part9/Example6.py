"""
    Создать в цикле замыкания
"""


def make_powers(count):
    powers = []
    for i in range(count):
        powers.append((lambda p: lambda x: x ** p)(i))
    return powers


powers = make_powers(5)
for power in powers:
    print(power(2))


"""
    Более простой вариант
"""


def make_powers_simple(count):
    powers = []
    for i in range(count):
        powers.append(lambda x, i=i: x ** i)
    return powers


powers = make_powers_simple(5)
for power in powers:
    print(power(2))