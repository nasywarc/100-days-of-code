# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def speak(self):
#         print('Meow')


# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def speak(self):
#         print('Bark')


# c1 = Cat('Kitty', 1)
# d1 = Dog('Doggy', 2)

# c1.speak()
# d1.speak()


# with inheritance
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f'I am {self.name} and I am {self.age} years old.')

    def speak(self):
        print('I dont know what to say.')


class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print('Meow.')

    def show(self):
        print(
            f'I am {self.name} and I am {self.age} years old and I am {self.color}.')


class Dog(Pet):
    def speak(self):
        print('Bark.')


class Fish(Pet):
    pass


c1 = Cat('Kitty', 1, 'White')
d1 = Dog('Doggy', 2)
f1 = Fish('Bubble', 3)

# same method in child from parents will override the method
c1.show()
c1.speak()
d1.show()
d1.speak()
f1.show()
f1.speak()
