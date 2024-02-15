def create_dict(dict):
    print('type :', type(dict), ', value = ', dict)


if __name__ == '__main__':
    create_dict({'name': 'John', 'occupation': 'dentist', 'age': 32})
    create_dict(dict(one=1, two=2, three=3))
    create_dict(dict([('one',1), ('two', 2), ('three', 3)]))
