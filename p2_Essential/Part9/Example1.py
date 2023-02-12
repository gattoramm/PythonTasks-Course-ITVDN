"""
    Функции первого класса
"""


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


def div(x, y):
    return x / y


operations = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div,
    '^': pow
}


try:
    first = float(input('First number: '))
    operation = input('Operation: ')
    second = float(input('Second number: '))
    result = operations[operation](first, second)
except ValueError:
    print('Incorrect input')
except KeyError:
    print('Unsupported operation')
except ZeroDivisionError:
    print('Division byzero')
else:
    print('Result:', result)
