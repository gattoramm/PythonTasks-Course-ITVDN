class ObjectWithDestructor:
    def __del__(self):
        print('Destructor ObjectWithDestructor')
        raise Exception


if __name__ == '__main__':
    print('Creating object...')
    obj2 = ObjectWithDestructor()
    print('Deleting reference...')
    del obj2
    print('Done ObjectWithDestructor')

