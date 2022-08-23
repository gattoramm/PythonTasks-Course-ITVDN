class MyObject(object):
    pass

print(type(MyObject))

class MyObject():
    pass

print(type(MyObject))

print(MyObject.__bases__)