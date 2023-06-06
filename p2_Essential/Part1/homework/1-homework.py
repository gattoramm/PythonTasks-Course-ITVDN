"""
    Создайте класс, описывающий книгу. Он должен содержать информацию об авторе, названии, годе
    издания и жанре. Создайте несколько разных книг. Определите для него операции проверки на
    равенство и неравенство, методы __repr__ и __str__.
"""


class Book:
    def __init__(self, author, name, age, type_book):
        self.author = author
        self.name = name
        self.age = age
        self.type_book = type_book
    
    def __repr__(self):
        return "Book(%s, %s, %s, %s)" % (self.author, self.name, self.age, self.type_book)
    
    def __str__(self):
        return 'Author = %s, Name = %s, Age = %d, Type = %s' % (self.author, self.name, self.age, self.type_book)
    
    def __eq__(self, other):
        return  self.author == other.author and\
                self.name == other.name and\
                self.age == other.age and\
                self.type_book == other.type_book
