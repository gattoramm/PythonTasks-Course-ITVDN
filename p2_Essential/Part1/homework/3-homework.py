"""
    Создайте класс, описывающий отзыв к книге. Добавьте в класс книги поле – список отзывов. Сделайте
    так, что при выводе книги на экран при помощи функции print также будут выводиться отзывы к ней.
"""


class Review:
    def __init__(self, review):
        self.review = review

    def __repr__(self):
        return self.review


class Book:
    def __init__(self, author, name, review=None):
        self.author = author
        self.name = name
        self.review = review

    def __repr__(self):
        return 'Book(%s, %s)' % (self.author, self.name)

    def __str__(self):
        return 'Book: Author = %s, Name = %s \nReview: %s' % (self.author, self.name, self.review)


if __name__ == "__main__":
    review1 = Review("Amazing!")
    review2 = Review("Cool")
    review3 = Review("Not bad")

    book1 = Book("King", "Scream", review1)
    book2 = Book("Hem", "Fish", review3)

    print(book1)
    print(book2)
