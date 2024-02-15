def get_hash(param):
    return hash(param)


if __name__ == '__main__':
    print('Hash of String \'hello\'\t:\t', get_hash('hello'))
    print('Hash of Typle (1, 2, 3)\t:\t', get_hash((1, 2, 3)))
    print('Hash of Float 3.55\t:\t', get_hash(3.55))
    print('Hash of Integer 355\t:\t', get_hash(355))
    print('Hash of Integer 1\t:\t', get_hash(1))
    print('Hash of Float 1.0\t:\t', get_hash(1.0))
    # print('Hash of List [1, 2, 3]\t:\t', get_hash([1, 2, 3])) #TypeError: unhashable type: 'list'
