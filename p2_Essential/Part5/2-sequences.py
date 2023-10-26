def print_seq(val):
    for _ in val:
        print(_)


if __name__ == "__main__":
    print("Print list:")
    print_seq([1, 5, 10])
    print("Print tuple:")
    print_seq((1, 5, 10))
    print("Print str:")
    print_seq('123')
    print("Print range:")
    print_seq(range(2, 6))
