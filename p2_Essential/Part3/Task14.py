import warnings

if __name__ == '__main__':
    name = input('Enter you name: ')

    if name.count(' ') != 1:
        warnings.warn('Name format was be incorrect')

    print('Hello,', name, '!', sep=' ')
