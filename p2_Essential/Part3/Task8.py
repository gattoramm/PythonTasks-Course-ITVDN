def main():
    try:
        raise ValueError('value is incorrect')
    except ValueError as error:
        raise ZeroDivisionError


if __name__ == '__main__':
    main()

