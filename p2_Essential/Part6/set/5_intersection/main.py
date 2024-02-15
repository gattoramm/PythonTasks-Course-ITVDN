vowels = {'a', 'o', 'e', 'i', 'u', 'y'}


if __name__ == '__main__':
    words = input('Enter a string: ').split(', ')

    for word in words:
        vowels.intersection_update(word.lower())

    print('\n'.join(vowels))