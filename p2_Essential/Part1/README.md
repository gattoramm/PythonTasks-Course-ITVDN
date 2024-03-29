### Введение в ООП

* Понятие ООП
* Создание классов
* Создание экземпляров классов
* Инкапсуляция
* Конструкторы и специальные методы в Python

#### Вопросы

* Что такое парадигма программирования?
  * Совокупность идей и понятий, определяющих стиль написания компьютерных программ, подход к программированию. 
* Назовите основные принципы объектно-ориентированного программирования.
  * Основные концепции - классы и объекты.
* Что такое класс?
  * Модель еще не существующей сущности (объекта). Составной тип данных, включающий поля и методы.
* Что такое объект?
  * Экземпляр класса.
* Что такое инкапсуляция?
  * Свойство системы, позволяющее объединить данные и методы, работающие с ними, в классе, и скрыть детали реализации.
* Что в Python не является объектом?
  * Все является объектами.
* Что такое атрибуты класса?
  * Члены класса - как переменные, так и функции.
* Что такое атрибуты экземпляров класса?
  * Атрибуты-данные и методы. Атрибуты-данные аналогичны полям, создаются в момент присваивания. Метод - функция,
  принадлежащая объекту.
* Чем отличаются обычные связанные методы, статические и методы класса?
  * Статический метод относятся к самому классу и всем его экземплярам и не принадлежит ни какому объекту-экземпляру
  (не имеет доступ к данным экземпляра класса).
  * Метод класса относятся к самому классу как объекту - экземпляру метакласса.
  * Обычные методы принадлежат объектам - экземплярам класса.
* Что такое специальные («магические») методы?
  * Задают особое поведение объектов и позволяют переопределять поведение встроенных функций и операторов для
  экземпляров данного класса.

#### Задания

* **Задание 1**

  Создайте класс, описывающий автомобиль. Создайте класс автосалона, содержащий в себе список
автомобилей, доступных для продажи, и функцию продажи заданного автомобиля.

* **Задание 2**

  Создайте класс, описывающий книгу. Он должен содержать информацию об авторе, названии, годе
издания и жанре. Создайте несколько разных книг. Определите для него операции проверки на
равенство и неравенство, методы `__repr__` и `__str__`.

* **Задание 3**

  Создайте класс, описывающий отзыв к книге. Добавьте в класс книги поле – список отзывов. Сделайте
так, что при выводе книги на экран при помощи функции `print` также будут выводиться отзывы к ней.

* **Задание 4**

  Ознакомьтесь с таким средством инкапсуляции как свойства. Ознакомьтесь с декоратором `property` в Python. Создайте
класс, описывающий температуру и позволяющий задавать и получать температуру по шкале Цельсия и Фаренгейта, причём
данные могут быть заданы в одной шкале, а получены в другой.