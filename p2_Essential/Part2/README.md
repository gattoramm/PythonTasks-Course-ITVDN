## Наследование и полиморфизм

### Вопросы

* Что такое наследование?
* Что такое множественное наследование?
* Каким образом в Python указать, что один класс наследуется от другого класса? От нескольких
других классов?
* Какие виды классов существуют в Python 2? В Python 3?
* Что такое MRO?
* Каким образом получить доступ к методу базового класса, если он был переопределён в
данном классе?
* Что такое полиморфизм?
* Что такое утиная типизация?

### Задания

**Задание 1**

Создайте иерархию классов транспортных средств. В общем классе опишите общие для всех
транспортных средств поля, в наследниках – специфичные для них. Создайте несколько экземпляров.
Выведите информацию о каждом транспортном средстве.

**Задание 2**

Создайте класс Editor, который содержит методы view_document и edit_document. Пусть метод
edit_document выводит на экран информацию о том, что редактирование документов недоступно для
бесплатной версии. Создайте подкласс ProEditor, в котором данный метод будет переопределён.
Введите с клавиатуры лицензионный ключ и, если он корректный, создайте экземпляр класса ProEditor,
иначе Editor. Вызовите методы просмотра и редактирования документов.

**Задание 3**

Опишите классы графического объекта, прямоугольника и объекта, который может обрабатывать
нажатия мыши. Опишите класс кнопки. Создайте объект кнопки и обычного прямоугольника. Вызовите
метод нажатия на кнопку.

**Задание 4**

Создайте иерархию классов с использованием множественного наследования. Выведите на экран
порядок разрешения методов для каждого из классов. Объясните, почему линеаризации данных
классов выглядят именно так.