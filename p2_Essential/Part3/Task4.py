class MyObject:
    def __del__(self):
        print('Destructor MyObject')
        print(self, 'is about be deleted')


if __name__ == '__main__':
    obj = MyObject()
    print(id(obj))
    ref = obj
    print(id(ref))
    print('del obj:')
    del obj
    print('del ref:')
    del ref



