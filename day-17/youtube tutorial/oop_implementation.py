class Person:
    person_count = 0

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
        Person.add()

    @classmethod
    def add(cls):
        cls.person_count += 1

    def show(self):
        print(
            f'Hello I\'m {self.name}, {self.age} years old, and i live in {self.address}')


p1 = Person('Brody', 23, 'Brooklyn')
p1.show()
