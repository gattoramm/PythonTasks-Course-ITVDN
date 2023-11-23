"""
    Опишите классы графического объекта, прямоугольника и объекта, который может обрабатывать нажатия мыши. Опишите
    класс кнопки. Создайте объект кнопки и обычного прямоугольника. Вызовите метод нажатия на кнопку.
"""


class GraphicObject:
    def __init__(self):
        print("Я - Графический объект")


class Rectangle:
    def __init__(self):
        print("Я - прямоугольник")
        self.name = "прямоугольник"


class ObjectForMouseEvent:
    def action(self):
        print("Я что-то делаю")


class Button:
    def __init__(self, button):
        self.button = button

    @classmethod
    def action(cls, obj):
        print("Я что-то делаю над", obj.name)
        return cls(obj)


if __name__ == "__main__":
    obj1 = GraphicObject()
    rect1 = Rectangle()
    button1 = Button.action(rect1)
