class MyObject:
    int_field = 8
    str_field = "string"

print(MyObject.int_field)
print(MyObject.str_field)

object1 = MyObject()
object2 = MyObject()

print(object1.int_field)
print(object2.str_field)

MyObject.int_field = 10

print(MyObject.int_field)
print(object1.int_field)

object2.str_field = "new_string"

print(MyObject.str_field)
print(object1.str_field)
print(object2.str_field)