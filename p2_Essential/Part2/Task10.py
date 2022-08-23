def check_instance(obj, cls):
    return check_subclass(type(obj), cls)


def check_subclass(child, base):
    return base in child.mro()


print(check_instance(8, int))
print(check_instance(8, str))
print(check_instance(True, int))
print(check_instance("8", object))
print()
print(check_subclass(bool, int))
print(check_subclass(bool, object))
print(check_subclass(bool, str))