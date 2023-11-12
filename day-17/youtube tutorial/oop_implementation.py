class Person:
    person_count = 0

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
        Person.add()

    def add(cls):
        Person.person_count += 1
