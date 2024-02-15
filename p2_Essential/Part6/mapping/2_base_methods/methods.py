if __name__ == '__main__':
    d = {'name': 'John', 'occupation': 'dentist', 'age': 32}
    print('d =', d)
    print('len(d) =', len(d))

    d['age'] = 777
    print('d[\'age\'] = 777, d =', d)

    print('keys of d:')
    for _ in d: print('\t', _)

    print('iter(d):', iter(d))
    print()

    print('d2 = d.copy()')
    d2 = d.copy()
    print('d2 =', d2)

    d['name'] = 'Mike'
    print('d[\'name\'] = \'Mike\', d =', d)
    print('d2 =', d2)
    print()

    print('fromkeys:')
    print(dict.fromkeys((1, 2, 3), 4))
    print()

    print('d2.get(\'name\') :', d2.get('name'))
    print('d2.get(\'new_name\') :', d2.get('new_name', 'empty'))
    print()

    di = d.items()
    print('d.items() :', di)
    print('d[\'name\'] = \'Mike2\'')
    d['name'] = 'Mike2'
    print('d =', d)
    print('d.items() :', di)
    for key, value in di:
        print(key + ':', value)
    print()

    dk = d.keys()
    print('d.keys() :', dk)
    print()

    dv = d.values()
    print('d.values() :', dv)
    print()

    print('d2.pop(\'name\') :', d2.pop('name'))
    print('d2 =', d2)
    print('d2.pop(\'new_name\') :', d2.pop('new_name', 'empty'))
    print('d2 =', d2)
    print()

    print('d.popitem() :', d.popitem())
    print('d =', d)
    print()

    print('d2.setdefault(\'age\') :', d2.setdefault('age'))
    print('d2 =', d2)
    print('d2.setdefault(\'new_name\') :', d2.setdefault('new_name', 'empty'))
    print('d2 =', d2)
    print()

    print('d.update(name=\'Kris\', city=\'Moscow\') :', d.update(name='Kris', city='Moscow'))
    print('d =', d)
