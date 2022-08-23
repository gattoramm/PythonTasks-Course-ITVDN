if __name__ == '__main__':
    a, b = 5, 0
    try:
        result = a / b
    except ZeroDivisionError as error:
        raise ValueError('variable b is incorrect') from error
