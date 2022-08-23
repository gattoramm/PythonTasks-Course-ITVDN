class MethodContainer:
    def __init__(self, data):
        self.data = data
    
    def method(self):
        print("in method")


instance = MethodContainer(8)
print("MethodContainer.method:", type(MethodContainer.method))
print("instance.method:", type(instance.method))

MethodContainer.method(instance)
instance.method()

print(MethodContainer.method)
print(instance.method)