if __name__ == '__main__':
    def do_stuff():
        try:
            raise ZeroDivisionError
        except ZeroDivisionError:
            print('Division by zero')

    try:
        do_stuff()
    # except AttributeError:
    #     print('Attribute error')
    except ValueError:
        print('ValueError error')
