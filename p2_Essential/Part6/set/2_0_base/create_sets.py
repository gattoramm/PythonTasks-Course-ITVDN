def create_set(set):
    print('type :', type(set), ', value = ', set)


if __name__ == '__main__':
    create_set(set())
    create_set(frozenset())
    create_set({3, 4, 5, 3})
    create_set(set({33, 44, 55, 33}))
    create_set(set((333, 444, 555, 333)))
    create_set(set([3333, 4444, 5555, 3333]))
    create_set(frozenset([4, 5, 6, 4]))
    create_set(frozenset((44, 55, 66, 44)))
    create_set(frozenset({444, 555, 666, 444}))
    create_set({})
    create_set({frozenset([4, 5, 6, 4]), frozenset((44, 55, 66, 44))})
    create_set({1, 1.0, 2, })
