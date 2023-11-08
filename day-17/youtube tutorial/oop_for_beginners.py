# # Object Oriented Programming in Python

# def hello():
#     print('hello')


# x = 1

# print(type(hello))
# print(type(x))


# string = 'hello'
# print(string.upper())
# # string method


# class Dog:

#     def __init__(self, name, age):
#         # make attribute
#         self.name = name
#         self.age = age

#     def get_name(self):
#         return self.name

#     def get_age(self):
#         return self.age

#     def set_age(self, age):
#         self.age = age


# d = Dog('Tim', 34)
# print(d.get_name())
# d.set_age(10)
# print(d.get_age())
# d2 = Dog('Bill', 12)
# print(d2.get_name())
# print(d2.get_age())


class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade  # 1- 100

    def get_grade(self):
        return self.grade


class Course:
    def __init__(self, name, max_student):
        self.name = name
        self.max_students = max_student
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()

        return value / len(self.students)


s1 = Student('Tim', 19, 95)
s2 = Student('Bill', 19, 75)
s3 = Student('Jill', 19, 65)

course = Course('Science', 2)
course.add_student(s1)
course.add_student(s2)
print(course.add_student(s3))
print(course.get_average_grade())
