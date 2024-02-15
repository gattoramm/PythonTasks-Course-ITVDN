def print_sets(*args):
    for i, k in enumerate(args):
        print('set{0} = {1}'.format(i + 1, k))


def print_len(*args):
    for i, k in enumerate(args):
        print('length of set{0} = {1}'.format(i+1, len(k)))


if __name__ == '__main__':
    s1 = {1, 234, 345345, 0, -45, 45, 0 , 999, -999, -1}
    s2 = {91, 234, -345345, 0, 45, -45, 0 , 55, -54, 6, -1, -1}
    s3 = {1, 0, -1}
    s4 = {100, 55, -100}

    print_sets(s1, s2, s3, s4)
    print()

    print("\t\tОПЕРАЦИИ С МНОЖЕСТВАМИ")

    print("len", end='')
    print(" - Количество элементов множества")
    print("=====================")
    print_len(s1, s2, s3, s4)
    print()

    print("in", end='')
    print(" - Нахождение элемента в множестве")
    print("=====================")
    print('999 in set 2 :', 999 in s2)
    print('999 in set 1 :', 999 in s1)
    print()

    print("not in", end='')
    print(" - Ненахождение элемента в множестве")
    print("=====================")
    print('999 in set 2 :', 55 not in s2)
    print('999 in set 1 :', 55 not in s1)
    print()

    print("isdisjoint", end='')
    print(" - Множество не имеет общих элементов с заданным")
    print("=====================")
    print('s4.isdisjoint(s2) :', s4.isdisjoint(s2))
    print('s4.isdisjoint(s1) :', s4.isdisjoint(s1))
    print('s3.isdisjoint(s1) :', s3.isdisjoint(s1))
    print()

    print("issubset", end='')
    print(" - Все элементы множества s являются элементами множества t (s.issubset(t))")
    print("=====================")
    print('s3.issubset(s2) :', s3.issubset(s2))
    print('s3.issubset(s1) :', s3.issubset(s1))
    print('with "<="')
    print('s3 <= s2 :', s3 <= s2)
    print('s3 <= s1 :', s3 <= s1)
    print()

    print("<", end='')
    print(" - Все элементы множества s являются элементами множества t и множества не равны (s.issubset(t))")
    print("=====================")
    print('s3 < s2 :', s3 < s2)
    print('s3 < s1 :', s3 < s1)
    print('s3 < s3 :', s3 < s3)
    print()

    print("issuperset", end='')
    print(" - Все элементы множества t являются элементами множества s (s.issuperset(t))")
    print("=====================")
    print('s2.issuperset(s3) :', s2.issuperset(s3))
    print('s1.issuperset(s3) :', s1.issuperset(s3))
    print('with ">="')
    print('s2 >= s3 :', s2 <= s3)
    print('s1 >= s3 :', s1 <= s3)
    print()

    print(">", end='')
    print(" - Все элементы множества t являются элементами множества s и множества не равны (s.issubset(t))")
    print("=====================")
    print('s2 > s3 :', s2 > s3)
    print('s1 > s3 :', s1 > s3)
    print('s3 > s3 :', s3 > s3)
    print()

    print("union", end='')
    print(" - Создание нового множества, которое является объединением данных множеств")
    print("=====================")
    print('s1.union(s2, s4, ) :', s1.union(s2, s4, ))
    print('s3.union(s4, ) :', s3.union(s4, ))
    print('s3.union(5) :', s3.union(list('5')))
    print('s3.union(5) :', s3.union([111, 222]))
    print('with "|"')
    print('s1 | s2 | s4 :', s1 | s2 | s4)
    print()

    print("intersection", end='')
    print(" - Создание нового множества, которое является пересечением данных множеств")
    print("=====================")
    print('s1.intersection(s2,) :', s1.intersection(s2,))
    print('s1.intersection(s3,) :', s1.intersection(s3,))
    print('s1.intersection(s3, s2, ) :', s1.intersection(s3, s2, ))
    print('s1.intersection(s4, ) :', s1.intersection(s4, ))
    print('with "|"')
    print('s1 & s2 :', s1 & s2)
    print('s1 & s3 :', s1 & s3)
    print('s1 & s2 & s3 :', s1 & s2 & s3)
    print('s1 & s4) :', s1 & s4)
    print()

    print("difference", end='')
    print(" - Создание нового множества, которое является разницей данных множеств")
    print("=====================")
    print('s1.difference(s2,) :', s1.difference(s2, ))
    print('s1.difference(s3,) :', s1.difference(s3, ))
    print('s1.difference(s3, s2, ) :', s1.difference(s3, s2, ))
    print('s1.difference(s4, ) :', s1.difference(s4, ))
    print('with "-"')
    print('s1 - s2 :', s1 -  s2)
    print('s1 - s3 :', s1 - s3)
    print('s1 - s2 & s3 :', s1 - s2 - s3)
    print('s1 - s4) :', s1 - s4)
    print()

    print("symmetric_difference", end='')
    print(" - Создание нового множества, которое является симметричной разницей данных множеств (разница объединения и пересечения множеств)")
    print("=====================")
    print('s1.symmetric_difference(s2, ) :', s1.symmetric_difference(s2, ))
    print('s1.symmetric_difference(s3, ) :', s1.symmetric_difference(s3, ))
    print('s2.symmetric_difference(s3, ) :', s2.symmetric_difference(s3, ))
    print('s3.symmetric_difference(s2, ) :', s3.symmetric_difference(s2, ))
    print('s1.symmetric_difference(s1) :', s1.symmetric_difference(s1))
    print('with "^"')
    print('s1 ^ s2 :', s1 ^ s2)
    print('s1 ^ s3 :', s1 ^ s3)
    print('s2 ^ s3 :', s2 ^ s3)
    print('s3 ^ s2 :', s3 ^ s2)
    print('s1 ^ s2 ^ s3 :', s1 ^ s2 ^ s3)
    print('s1 ^ s1 :', s1 ^ s1)

    print("==========================================")
    print("Сами множества не изменились")
    print_sets(s1, s2, s3, s4)
