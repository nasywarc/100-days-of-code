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

    def __init__(self, name):
        self.name = name
        # make attribute


d = Dog('Tim')
print(d.name)
d2 = Dog('Bill')
print(d2.name)
