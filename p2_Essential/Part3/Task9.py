if __name__ == '__main__':
    value_error = ValueError()
    value_error.__context__ = ZeroDivisionError()
    raise value_error
