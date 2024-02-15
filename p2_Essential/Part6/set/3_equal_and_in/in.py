if __name__ == '__main__':
    print('{1, 2, 3} == {3, 2, 1, 3, 1} :', {1, 2, 3} == {3, 2, 1, 3, 1})
    print('{1, 2, 3} == {5, 2, 1, 5, 1} :', {1, 2, 3} == {5, 2, 1, 5, 1})
    print('{1, 2, 3} == frozenset({1, 2, 3}) :', {1, 2, 3} == frozenset({1, 2, 3}))
    print('{1, 2, 3} == frozenset({3, 2, 1, 3, 1}) :', {1, 2, 3} == frozenset({3, 2, 1, 3, 1}))
    print('{1, 2} in { frozenset([1]), frozenset([2, 1]), } :', {1, 2} in { frozenset([1]), frozenset([2, 1]), })
