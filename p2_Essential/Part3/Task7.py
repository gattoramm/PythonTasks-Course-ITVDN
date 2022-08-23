def main():
    try:
        raise ValueError('value is incorrect')
    except ValueError as error:
        print('Exception: ', error)
        raise


if __name__ == '__main__':
    # try:
        main()
    # except ValueError:
    #     print('ValueError detected')
