if __name__ == '__main__':
    print('add', end='')
    print(' - Добавить новый элемент в множество - s.add(element)')

    s = {0, 1, 2, 3, str(110)}
    print('s =', s)

    print("s.add('111') = ", end='')
    s.add('111')
    print(s)
    print()

    print('remove', end='')
    print(' - Удалить элемент из множества; если такого элемента нет, возникает KeyError - s.remove(element)')

    s = {0, 1, 2, 3, str(110)}
    print("s.remove('110') = ", end='')
    s.remove('110')
    print(s)

    print("s.remove('110') = ", end='')
    try:
        s.remove('110')
    except KeyError:
        print('Возникло исключение: удаляемого элемента нет в множестве')
    print()

    print('discard', end='')
    print(' - Удалить элемент из множества, если онв нем находится - s.discard(element)')

    s = {0, 1, 2, 3, str(110)}
    print("s.discard('111') = ", end='')
    s.discard('111')
    print(s)
    print()

    print('pop', end='')
    print(' - Удалить из множества и вернуть произвольный элемент (KeyError, если пустое) - s.pop(element)')

    s = {0, 1, 2, 3, str(110)}
    print("s.pop() = ", end='')
    print(s.pop())
    print('s = ', s)

    s = set()
    print('s =', s)
    print("s.pop() = ", end='')
    try:
        p = s.pop()
    except KeyError:
        print('Возникло исключение: пустое множество')
    print()

    print('clear', end='')
    print(' - Удалить все элементы множества - s.clear()')

    s = {0, 1, 2, 3, str(110)}
    print("s.pop() -> ", end='')
    s.clear()
    print('s =', s)
