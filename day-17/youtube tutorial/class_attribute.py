# # classmethod implementation
# class Person:
#     number_of_people = 0

#     def __init__(self, name):
#         self.name = name
#         Person.add_person()

#     @classmethod
#     def number_of_people_(cls):
#         return cls.number_of_people

#     @classmethod
#     def add_person(cls):
#         cls.number_of_people += 1


# p1 = Person('Tim')
# print(Person.number_of_people_())
# p2 = Person('Jack')
# print(Person.number_of_people_())


# staticmethod implementation
class Math:
    @staticmethod
    def add5(x):
        return x + 5

    def add10(x):
        return x + 10

    def pr():
        print('run')


print(Math.add5(5))
print(Math.add10(5))
Math.pr()
