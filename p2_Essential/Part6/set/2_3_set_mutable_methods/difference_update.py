if __name__ == '__main__':
    print('difference_update', end='')
    print(" - Удалить из данного множества те элементы, которые есть в других множествах")
    print("'s.difference_update(t, ...)' или 's -= t - ...'")
    print()

    s1 = {0, 1, 2, 3, str(110)}
    s2 = {-1, 1, 0, 77, '110'}
    f = frozenset((-1, 1, 0, 77, '110'))
    print('s1 =', s1, ', s2 =', s2, ', f =', f)
    print()

    print("s1.difference_update(s2, ) = ", end='')
    s1.difference_update(s2, )
    print(s1)

    s1 = {0, 1, 2, 3, str(110)}
    print("s2.difference_update(s1, ) = ", end='')
    s2.difference_update(s1, )
    print(s2)

    s1 = {0, 1, 2, 3, str(110)}
    s2 = {-1, 1, 0, 77, '110'}
    print("s1.difference_update(s2, [3, '110', '3'], ) = ", end='')
    s1.difference_update(s2, [3, '110', '3'], )
    print(s1)

    s1 = {0, 1, 2, 3, str(110)}
    print("s1.difference_update(s1, ) = ", end='')
    s1.difference_update(s1, )
    print(s1)
    print()

    s1 = {0, 1, 2, 3, str(110)}
    print("s1.difference_update(f) = ", end='')
    s1.difference_update(f, )
    print(s1)
    print()

    print('With "-="')
    s1 = {0, 1, 2, 3, str(110)}
    print("s1 -= f - {3, '110', '3'} = ", end='')
    s1 -= f - {3, '110', '3'}
    print(s1)

    s1 = {0, 1, 2, 3, str(110)}
    print("s1 -= {3, '110', '3'} - f = ", end='')
    s1 -= {3, '110', '3'} - f
    print(s1)

    s1 = {0, 1, 2, 3, str(110)}
    print("s1 -= s1 = ", end='')
    s1 -= s1
    print(s1)
