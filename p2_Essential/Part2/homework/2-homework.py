"""
    Создайте класс `Editor`, который содержит методы `view_document` и `edit_document`. Пусть метод `edit_document`
    выводит на экран информацию о том, что редактирование документов недоступно для бесплатной версии. Создайте
    подкласс `ProEditor`, в котором данный метод будет переопределён. Введите с клавиатуры лицензионный ключ и, если
    он корректный, создайте экземпляр класса `ProEditor`, иначе `Editor`. Вызовите методы просмотра и редактирования
    документов.

"""


class Editor:
    def view_document(self):
        print("просмотр документов...")

    def edit_document(self):
        print("редактирование документов недоступно для бесплатной версии")


class ProEditor(Editor):
    def edit_document(self):
        print("редактирование документов...")


if __name__ == "__main__":
    key = input("Введите ключ: ")
    if key == "qwerty":
        editor = ProEditor()
    else:
        editor = Editor()
    editor.view_document()
    editor.edit_document()
