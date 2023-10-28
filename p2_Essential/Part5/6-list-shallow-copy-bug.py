def print_matrix(matrix):
    for row in matrix:
        print(' '.join(str(x) for x in row))


if __name__ == "__main__":
    print_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    a = [[0] * 5] * 5
    print(a)
    print_matrix(a)
    a[1][3] = 1
    print_matrix(a)
    print(a[0] is a[1])
    aa = [[0] * 5 for _ in range(5)]
    print_matrix(aa)
    aa[1][3] = 1
    print_matrix(aa)
