def main():
    while True:
        try:
            first_num = float(input('First number: '))
            second_num = float(input('Second number: '))
            result = first_num / second_num
            print('Result : ', result)
            break
        except (ValueError, ZeroDivisionError) as error:
            print('Error: ', error)
            print('Please try again')
            print()


if __name__ == '__main__':
    main()
