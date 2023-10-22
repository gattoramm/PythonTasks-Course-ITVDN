def check_instance(obj, cls):
    return check_subclass(type(obj), cls)


def check_subclass(child, base):
    if child == base:
        return True
    for direct_base in child.__bases__:
        if base == direct_base:
            return True
        return check_subclass(direct_base, base)
    return False


if __name__ == "__main__":
    print('object.__bases__: ', object.__bases__)
    print('check_subclass(bool, int):', check_subclass(bool, int))
    print('check_subclass(bool, str):', check_subclass(bool, str))
    print('check_subclass(bool, object):', check_subclass(bool, object))
    print('check_subclass(bool, bool):', check_subclass(bool, bool))
    print('check_instance(8, int): ', check_instance(8, int))
    print()
    print('isinstance(8, int): ', isinstance(8, int))
    print('issubclass(bool, bool): ', issubclass(bool, bool))
    print('isinstance(object, type): ', isinstance(object, type))
    print('isinstance(int, type): ', isinstance(int, type))
