class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    def __str__(self):
        return '[Person: %s %s]' % (self.name, self.pay)


class Manager(Person):
    def __init__(self, name, pay):
        Person.__init__(self, name, 'mgr', pay)

    def giveRaise(self, percent, bonus=.10):
        Person.giveRaise(self, percent + bonus)


class Department:
    def __init__(self, *args):
        self.members = list(args)

    def addMember(self, person):
        self.members.append(person)

    def giveRaises(self, percent):
        for person in self.members:
            person.giveRaise(percent)

    def showAll(self):
        for person in self.members:
            print(person)


name1 = 'bob smith'
print(name1.split()[-1])

# pay = 100000
# pay *= 1.10
# print(pay)

if __name__ == '__main__':
    bob = Person('bob smith')
    sue = Person('sue jones', job='dev', pay=100000)
    # man = Manager('man manager', job='manager', pay=50000)
    # man.giveRaise(.10)

    print(bob.name, bob.pay, bob.job)
    print(sue.name, sue.job)
    print(bob.lastName(), sue.lastName())  # Вместо жестко определенных
    sue.giveRaise(.10)  # операций используются методы
    print(sue.pay)
    print(sue)
    tom = Manager('tom jones', 50000)
    tom.giveRaise(.10)
    print(tom.lastName())
    print(tom)
    development = Department(bob, sue)  # Встраивание объектов в составной объект
    development.addMember(tom)
    development.giveRaises(.10)  # Вызов метода giveRaise вложенных объектов
    development.showAll()
