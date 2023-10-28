if __name__ == "__main__":
    empty_tuple = ()
    print('value=', empty_tuple, ', type=', type(empty_tuple))
    person = ('John', 30)
    print('value=', person, ', type=', type(person))
    a = tuple(range(3))
    print('value=', a, ', type=', type(a))
    b = 1,
    print('value=', b, ', type=', type(b))
    c = 1, 2, 'a'
    print('value=', c, ', type=', type(c))
    d = (1, 2) * 3
    print('value=', d, ', type=', type(d))
    e = ['a', 'b', 'e']
    f = [3000, 2000, 10000]
    ef = zip(e, f)
    print('value=', ef, ', type=', type(ef))
    ef_l = list(ef)
    print('value=', ef_l, ', type=', type(ef_l))
    g = enumerate(e)
    g_l = list(g)
    print('value=', g_l, ', type=', type(g_l))
    g2 = enumerate(e, 1)
    g_l2 = list(g2)
    print('value=', g_l2, ', type=', type(g_l2))
    a, b, c = 1, 2, 3
    print(a, b, c)
    a, b, c = 'abc'
    print(a, b, c)
    head, *tail = range(10)
    print(head, tail)
    *head, tail = range(10)
    print(head, tail)
    first, second, *middle, last = range(10)
    print(first, second, middle, last)
    x = 2
    y = 5
    x, y = y, x
    print(x, y)
