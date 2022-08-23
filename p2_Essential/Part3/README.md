## Исключения

### Вопросы

* Что такое исключительная ситуация (исключение)?
* Какой оператор в Python предназначен для обработки исключений?
* Какие его основные блоки? Какое их назначение?
* Какой оператор в Python предназначен для выброса исключений?
* Чем отличается создание объекта исключения от выброса исключения?
* Каким образом можно получить экземпляр обрабатываемого исключения?
* Каким образом задать одинаковый обработчик для нескольких разных исключений?
* От какого класса наследуются все исключения?
* Что такое сцепление исключений?
* Что такое синтаксическая ошибка?
* Что такое предупреждение и как его сгенерировать?

### Задания

**Задание 1**

Опишите свой класс исключения. Напишите функцию, которая будет выбрасывать данное исключение,
если пользователь введёт определённое значение, и перехватите это исключение при вызове функции.

**Задание 2**

Напишите программу-калькулятор, которая поддерживает следующие операции: сложение, вычитание,
умножение, деление и возведение в степень. Программа должна выдавать сообщения об ошибке и
продолжать работу при вводе некорректных данных, делении на ноль и возведении нуля в
отрицательную степень.

**Задание 3**

Опишите класс сотрудника, который включает в себя такие поля, как имя, фамилия, отдел и год
поступления на работу. Конструктор должен генерировать исключение, если заданы неправильные
данные. Введите список работников с клавиатуры. Выведите всех сотрудников, которые были приняты
после заданного года.