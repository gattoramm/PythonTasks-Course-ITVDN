"""
    Замыкания
"""


def add(x):
    def do_add(y):
        return x + y
    return do_add


print(add(5)(3))

add_to_five = add(5)

print(add_to_five(3))
print(add_to_five(4))
print(add_to_five(5))
