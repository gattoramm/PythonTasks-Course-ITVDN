_function = {}

def register(f):
    global _function
    _function[f.__name__] = f
    return f

@register
def foo():
    return 'bar'

ff = foo()
print(ff)