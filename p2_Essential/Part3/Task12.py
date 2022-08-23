MAX_STARS = 32
WIDTH = 40


def print_result(number):
    if number == 0:
        stars_count = MAX_STARS
    else:
        stars_count = round(MAX_STARS / number)
        if stars_count > WIDTH:
            stars_count = WIDTH

    number_field_width = WIDTH - 2 * stars_count
    stars = '*' * stars_count
    fmt = '{0}{1:^' + str(number_field_width) + '}{0}'
    print(fmt.format(stars, number))


def divide_numbers():
    while True:
        try:
            first_num = float(input('First number: '))
            second_num = float(input('Second number: '))
            result = first_num / second_num
        except (ValueError, ZeroDivisionError) as error:
            print('Error: ', error)
            print('Please try again')
            print()
        else:
            print_result(result)
            break


if __name__ == '__main__':
    divide_numbers()
