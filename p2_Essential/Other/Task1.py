class Person:
    def __init__(self, name, age, pay=0, job=None):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)


class Manager(Person):
    def giveRaise(self, percent, bonus=0.2):
        Person.giveRaise(self, percent + bonus)


if __name__ == '__main__':
    bob = Person(name='Bob Smith', age=42, pay=10000)
    sue = Person(name='Sue Jones', age=45, pay=20000)
    tom = Manager(name='Nom Doe', age=55, pay=30000)

    db = [bob, sue, tom]

    for obj in db:
        obj.giveRaise(.10)

    for obj in db:
        print(obj.lastName(), '=>', obj.pay)