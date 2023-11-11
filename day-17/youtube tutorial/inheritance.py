class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print('Meow')


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print('Bark')


c1 = Cat('Kitty', 1)
d1 = Dog('Doggy', 2)

c1.speak()
d1.speak()
