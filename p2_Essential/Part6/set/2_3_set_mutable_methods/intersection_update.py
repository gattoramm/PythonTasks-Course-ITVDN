if __name__ == '__main__':
    print('intersection_update', end='')
    print(" - Оставить в данном множестве только те элементы, которые есть и в других множествах")
    print("'s.intersection_update(t, ...)' или 's &= t & ...'")
    print()

    s1 = {0, 1, 2, 3, str(110)}
    s2 = {-1, 1, 0, 77, '110'}
    f = frozenset((-1, 1, 0, 77, '110'))
    print('s1 =', s1, ', s2 =', s2, ', f =', f)
    print()

    print("s1.intersection_update(s2, {0, 5, 1, 77, '110'}, ) = ", end='')
    s1.intersection_update(s2, {0, 5, 1, 77, '110'}, )
    print(s1)

    s1 = {0, 1, 2, 3, str(110)}
    print("s2.intersection_update(s1, {0, 5, 1, 77, '110'}, ) = ", end='')
    s2.intersection_update(s1, {0, 5, 1, 77, '110'}, )
    print(s2)

    s1 = {0, 1, 2, 3, str(110)}
    s2 = {-1, 1, 0, 77, '110'}
    print("s1.intersection_update(s2, ['77', '110'], ) = ", end='')
    s1.intersection_update(s2, ['77', '110'], )
    print(s1)

    s1 = {0, 1, 2, 3, str(110)}
    print("s1.intersection_update(s1) = ", end='')
    s1.intersection_update(s1)
    print(s1)
    print()

    print("s1.intersection_update(f) = ", end='')
    s1.intersection_update(f, )
    print(s1)
    print()

    print('With "&"')
    s1 = {0, 1, 2, 3, str(110)}
    print("s1 &= f & {'77', '110'} = ", end='')
    s1 &= f & {'77', '110'}
    print(s1)

    s1 = {0, 1, 2, 3, str(110)}
    print("s1 &= {'77', '110'} & f = ", end='')
    s1 &= {'77', '110'} & f
    print(s1)

    s1 = {0, 1, 2, 3, str(110)}
    print("s1 &= s1 = ", end='')
    s1 &= s1
    print(s1)
