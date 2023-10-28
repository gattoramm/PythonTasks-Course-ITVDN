def change_item(data, index, value):
    data[index] = value
    return data


def change_item2(data, index, value):
    data.__setitem__(index, value)
    return data


if __name__ == "__main__":
    values = [5, 1, 2, 8, 4, 2, 9, 0]
    print("values = ", values)
    print('\t\tchange')
    change_item(values, 2, 42)
    print("values = ", values)
    change_item2(values, 1, 41)
    print("values = ", values)
    print('\t\tslice')
    values[:4] = range(4)
    print("values = ", values)
    values[-1:] = [5, 1, 2, 5]
    print("values = ", values)
    values[3:8] = []
    print("values = ", values)
    values[3:3] = [0] * 5
    print("values = ", values)
    print('\t\tdel')
    del values[0]
    print("values = ", values)
    del values[:3]
    print("values = ", values)
    del values[::2]
    print("values = ", values)
    values.__delitem__(-1)
    print("values = ", values)
    print('\t\tappend')
    values.append(8)
    print("values = ", values)
    values[len(values):] = [9]
    print("values = ", values)
    print('\t\textend')
    values.extend(range(3))
    print("values = ", values)
    print('\t\tcopy')
    list_ = values
    print(values is list_)
    values.append(77)
    print("list_ = ", list_)
    list_ = values.copy()
    print(values is list_)
    values.append(78)
    print("values = ", values)
    print("list_ = ", list_)
    print('\t\tcopy')
    values.insert(3, 999)
    print("values = ", values)
    values.insert(999, 999)
    print("values = ", values)
    values.insert(-999, 999)
    print("values = ", values)
    print('\t\tpop')
    x = values.pop()
    print("x = ", x)
    x = values.pop(5)
    print("x = ", x)
    print('\t\tremove')
    print("values = ", values)
    values.remove(999)
    print("values = ", values)
    values.remove(999)
    print("values = ", values)
    print('\t\tclear')
    print("values = ", values)
    values.clear()
    print("values = ", values)

