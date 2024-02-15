if __name__ == '__main__':
    print('update', end='')
    print(" - Добавить в данное множество элементы из других множеств")
    print("'s.update(t, ...)' или 's |= t | ...'")
    print()

    s1 = {1, 2, 3, 10, 1}
    s2 = {10, 20, 30, 1}
    f = frozenset((1, 2, 3))

    print('s1 =', s1, ', s2 =', s2, ', f =', f)
    print()

    print('s1.update(s2, {0, 5}, ) = ', end='')
    s1.update(s2, {0, 5, }, )
    print(s1)
    s1 = {1, 2, 3, 10, 1}
    print('s2.update(s1, {0, 5, }, ) = ', end='')
    s2.update(s1, {0, 5, }, )
    print(s2)

    print("s1.update([44, 777], list('python'), 'java', ['PYTHON'], = ", end='')
    s1.update([44, 777], list('python'), 'java', ['PYTHON'], )
    print(s1)

    s1 = {1, 2, 3, 10, 1}
    print("s1.update(s1) = ", end='')
    s1.update(s1)
    print(s1)
    print()

    s1 = {1, 2, 3, 10, 1}
    print('s1.update(f, frozenset((9, 8, 7)), ) = ', end='')
    s1.update(f, frozenset((9, 8, 7)), 'ABC', [55, 44, 'BB'], )
    print(s1)
    print()

    print('With "|="')
    s1 = {1, 2, 3, 10, 1}
    f = frozenset((1, 2, 3))
    print('s1 |= {0, 5} | f = ', end='')
    s1 |= {0, 5} | f
    print(s1)

    s1 = {1, 2, 3, 10, 1}
    print('s1 |= f | {0, 5} = ', end='')
    s1 |= f | {0, 5}
    print(s1)

    s1 = {1, 2, 3, 10, 1}
    print('s1 |= s1 = ', end='')
    s1 |= s1
    print(s1)
