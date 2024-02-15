def order():
    return {x ** 2 for x in range(1, 11)}


if __name__ == '__main__':
    result = order()
    print(result)
