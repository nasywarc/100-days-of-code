class Person:
    person_count = 0

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
        Person.add()

    def show(self):
        print(
            f'Hello I\'m {self.name}, {self.age} years old, and i live in {self.address}.')

    @classmethod
    def add(cls):
        cls.person_count += 1

    @classmethod
    def show_person_count(cls):
        return cls.person_count


class Seller(Person):
    def __init__(self, name, age, address, store_name):
        super().__init__(name, age, address)
        self.store_name = store_name


class Buyer(Person):
    def __init__(self, name, age, address, payment):
        super().__init__(name, age, address)
        self.payment = payment


s1 = Seller('Tony', 31, 'London', 'Elecstore')
b1 = Buyer('Rick', 18, 'Manchester', 'cash')

# p1 = Person('Brody', 23, 'Brooklyn')
# p1.show()
# print(Person.show_person_count())
