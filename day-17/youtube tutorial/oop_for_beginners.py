# # Object Oriented Programming in Python

# def hello():
#     print('hello')


# x = 1

# print(type(hello))
# print(type(x))


# string = 'hello'
# print(string.upper())
# # string method

class Dog:

    def add_one(self, x):
        return x + 1

    def bark(self):
        print('bark')


d = Dog()
print(type(d))
# use a method on the instance
d.bark()
print(d.add_one(5))
