if __name__ == '__main__':
    print('symmetric_difference_update', end='')
    print(" - Оставить или добавить в s элементы, которые есть либо в s, либо в t, но не в обоих множествах")
    print("'s.symmetric_difference_update(t)' или 's ^= t'")
    print()

    s1 = {0, 1, 2, 3, str(110)}
    s2 = {-1, 1, 0, 77, '110'}
    f = frozenset((-1, 1, 0, 77, '110', -2))
    print('s1 =', s1, ', s2 =', s2, ', f =', f)
    print()

    print("s1.symmetric_difference_update(s2, ) = ", end='')
    s1.symmetric_difference_update(s2, )
    print(s1)

    s1 = {0, 1, 2, 3, str(110)}
    print("s2.symmetric_difference_update(s1, ) = ", end='')
    s2.symmetric_difference_update(s1, )
    print(s2)

    s1 = {0, 1, 2, 3, str(110)}
    print("s1.symmetric_difference_update(s1, ) = ", end='')
    s1.symmetric_difference_update(s1, )
    print(s1)
    print()

    s2 = {-1, 1, 0, 77, '110'}
    print("s2.symmetric_difference_update(f) = ", end='')
    s2.symmetric_difference_update(f)
    print(s2)
    print()

    print('With "^="')
    s1 = {0, 1, 2, 3, str(110)}
    s2 = {-1, 1, 0, 77, '110'}
    print("s1 ^= s2 = ", end='')
    s1 ^= s2
    print(s1)

    s1 = {0, 1, 2, 3, str(110)}
    print("s2 ^= s1 = ", end='')
    s2 ^= s1
    print(s2)

    print("s1 ^= s1 = ", end='')
    s1 ^= s1
    print(s1)
