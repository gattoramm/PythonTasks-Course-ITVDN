if __name__ == '__main__':
    # value_error = ValueError()
    # value_error.__cause__ = ZeroDivisionError()
    # raise value_error

    raise ValueError from ZeroDivisionError
