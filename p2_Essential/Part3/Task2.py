if __name__ == '__main__':
    print('Calculator')
    try:
        a = float(input('a = '))
        b = float(input('b = '))
        print(a/b)
    except (ZeroDivisionError, ValueError) as error:
        print(error)
